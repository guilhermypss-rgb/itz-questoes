import json, sys, re, math, unicodedata, fractions, statistics

CARGOS = {"RAD", "FIS", "PSI", "GMI", "TRA"}
FMT = {"unica", "afirmativas", "vf", "associacao", "excecao"}
NIV = {"facil", "medio", "dificil"}
BAD = re.compile(r"todas as (alternativas|anteriores|acima)|nenhuma das (alternativas|anteriores|acima)", re.I)


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\W+", " ", s).strip()


def num(s):
    s = s.replace("R$", "").replace(" ", "")
    m = re.search(r"-?\d[\d.]*(?:,\d+)?", s)
    if not m:
        return None
    t = m.group(0)
    if "," in t:
        t = t.replace(".", "").replace(",", ".")
    elif re.fullmatch(r"-?\d{1,3}(\.\d{3})+", t):
        t = t.replace(".", "")
    try:
        return float(t)
    except ValueError:
        return None


SAFE = {"math": math, "Fraction": fractions.Fraction, "sum": sum, "range": range, "round": round,
        "abs": abs, "min": min, "max": max, "len": len, "sqrt": math.sqrt, "comb": math.comb,
        "perm": math.perm, "factorial": math.factorial, "mean": statistics.mean, "pi": math.pi}


def check(q):
    e = []
    need = ["id", "cargos", "disciplina", "topico", "nivel", "formato", "enunciado",
            "alternativas", "gabarito", "comentario", "fonte", "confianca"]
    for k in need:
        if k not in q or q[k] in ("", None, []):
            e.append("falta " + k)
    if e:
        return e
    if not set(q["cargos"]) <= CARGOS:
        e.append("cargo invalido")
    if q["formato"] not in FMT:
        e.append("formato invalido")
    if q["nivel"] not in NIV:
        e.append("nivel invalido")
    if q["confianca"] not in ("alta", "media", "baixa"):
        e.append("confianca invalida")
    a = q["alternativas"]
    if not (isinstance(a, list) and len(a) == 5 and all(isinstance(x, str) and x.strip() for x in a)):
        return e + ["precisa 5 alternativas"]
    if len({norm(x) for x in a}) != 5:
        e.append("alternativas repetidas")
    if q["gabarito"] not in list("ABCDE"):
        e.append("gabarito invalido")
    if any(re.match(r"^\s*[a-eA-E][\)\.]\s", x) for x in a):
        e.append("alternativa com letra no texto")
    if BAD.search(" ".join(a) + " " + q["enunciado"]):
        e.append("todas/nenhuma das anteriores")
    if len(q["comentario"]) < 60:
        e.append("comentario curto")
    if q["formato"] == "vf":
        n = q["enunciado"].count("( )")
        if n not in (3, 4):
            e.append("vf precisa 3 ou 4 itens '( )'")
        else:
            for x in a:
                if not re.fullmatch(r"[VF]( – [VF]){%d}" % (n - 1), x.strip()):
                    e.append("vf sequencia fora do padrao: " + x)
                    break
    if q["formato"] == "afirmativas" and not re.search(r"(^|\n)I\. ", q["enunciado"]):
        e.append("afirmativas sem itens I.")
    if q["disciplina"] == "LP":
        w = len(q.get("texto_base", "").split())
        if not 140 <= w <= 320:
            e.append(f"texto_base {w} palavras")
        if not q.get("texto_id"):
            e.append("LP sem texto_id")
    if q.get("calculo"):
        try:
            v = eval(str(q["calculo"]), {"__builtins__": {}}, SAFE)
            n = num(a["ABCDE".index(q["gabarito"])])
            if n is None or abs(float(v) - n) > max(1e-2, abs(n) * 1e-3):
                e.append(f"calculo {v} != alternativa {n}")
        except Exception as ex:
            e.append("calculo erro " + str(ex))
    return e


def load(paths):
    good, bad, seen = [], [], {}
    for p in paths:
        with open(p, encoding="utf-8") as f:
            for i, l in enumerate(f, 1):
                l = l.strip()
                if not l:
                    continue
                try:
                    q = json.loads(l)
                except Exception as ex:
                    bad.append(f"{p}:{i}: json {ex}")
                    continue
                er = check(q)
                h = norm(q.get("enunciado", "") + " " + q.get("texto_base", "")[:200]) + "|" + norm(" ".join(map(str, q.get("alternativas", []))))
                h2 = q.get("id")
                if h in seen:
                    er.append("duplicada de " + str(seen[h]))
                if ("id:" + str(h2)) in seen:
                    er.append("id repetido")
                seen[h] = h2
                seen["id:" + str(h2)] = 1
                if er:
                    bad.append(f"{p}:{i}:{h2}: " + "; ".join(er))
                else:
                    good.append(q)
    return good, bad


if __name__ == "__main__":
    good, bad = load(sys.argv[1:])
    for b in bad[:60]:
        print(b)
    print(f"validas={len(good)} invalidas={len(bad)}")
    sys.exit(1 if bad else 0)
