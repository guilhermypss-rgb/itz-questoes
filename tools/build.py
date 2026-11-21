"""Junta lotes validados -> site/questoes.json + RELATORIO.md. Uso: python tools/build.py"""
import json, glob, sys, os, collections
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "data"))
from validate import load
from topics import DISC

root = os.path.join(os.path.dirname(__file__), "..")
good, bad = load(sorted(glob.glob(os.path.join(root, "lotes", "*.jsonl"))))
textos, out = {}, []
for q in good:
    q = dict(q)
    q.pop("_embaralhada", None)
    tb = q.pop("texto_base", None)
    if tb:
        textos[q["texto_id"]] = tb
    out.append(q)
os.makedirs(os.path.join(root, "site"), exist_ok=True)
json.dump({"textos": textos, "questoes": out}, open(os.path.join(root, "site", "questoes.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

C = collections.Counter
L = ["# Relatório do banco de questões\n", f"Questões válidas: **{len(out)}** (meta 20.000). Inválidas descartadas: {len(bad)}.\n"]
L.append("## Por disciplina (meta x feito)\n\n| Disciplina | Meta | Feito | % |\n|---|---|---|---|")
bd = C(q["disciplina"] for q in out)
for k, (nome, meta, _, _) in DISC.items():
    L.append(f"| {nome} | {meta} | {bd[k]} | {100*bd[k]/meta:.1f}% |")
L.append("\n## Por cargo (questões utilizáveis)\n")
bc = C(c for q in out for c in q["cargos"])
for k, v in sorted(bc.items()):
    L.append(f"- {k}: {v}")
for tit, key in (("Formato", "formato"), ("Nível", "nivel"), ("Confiança", "confianca")):
    c = C(q[key] for q in out)
    L.append(f"\n## {tit} (alvo formato: unica 75%, afirmativas 12%, vf 9%, associacao 2%, excecao ≤2%; nível 30/50/20)\n")
    for k, v in c.most_common():
        L.append(f"- {k}: {v} ({100*v/len(out):.1f}%)")
L.append("\n## Gabarito (deve ser ~20% cada)\n")
g = C(q["gabarito"] for q in out)
L.append(", ".join(f"{k}: {g[k]}" for k in "ABCDE"))
# viés de tamanho: certa é a mais longa?
uni = [q for q in out if q["formato"] == "unica"]
mais = sum(1 for q in uni if max(range(5), key=lambda i: len(q["alternativas"][i])) == "ABCDE".index(q["gabarito"]))
L.append(f"\nCerta é a mais longa em {mais} de {len(uni)} questões 'unica' ({100*mais/max(1,len(uni)):.0f}%; ideal ≈20-30%).")
L.append("\n## Por tópico\n\n| Disciplina | Tópico | Qtd |\n|---|---|---|")
bt = C((q["disciplina"], q["topico"]) for q in out)
for k, (nome, meta, _, tops) in DISC.items():
    for t in tops:
        L.append(f"| {k} | {t} | {bt[(k, t)]} |")
if bad:
    L.append("\n## Inválidas\n")
    L += [f"- {b}" for b in bad[:50]]
open(os.path.join(root, "RELATORIO.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print(len(out), "questoes;", len(bad), "invalidas; site/questoes.json",
      round(os.path.getsize(os.path.join(root, "site", "questoes.json")) / 1e6, 2), "MB")
