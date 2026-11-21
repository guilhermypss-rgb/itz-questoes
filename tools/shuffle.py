"""Embaralha alternativas (posição aleatória do gabarito). Uso: python tools/shuffle.py arquivo.jsonl
Não embaralha MAT nem questões com "ordenada": true (alternativas numéricas/ordem lógica)."""
import json, sys, random

for p in sys.argv[1:]:
    out = []
    for l in open(p, encoding="utf-8"):
        l = l.strip()
        if not l:
            continue
        q = json.loads(l)
        if not q.get("_embaralhada") and q.get("disciplina") != "MAT" and not q.get("ordenada"):
            idx = list("ABCDE").index(q["gabarito"])
            order = list(range(5))
            random.shuffle(order)
            q["alternativas"] = [q["alternativas"][i] for i in order]
            q["gabarito"] = "ABCDE"[order.index(idx)]
        q["_embaralhada"] = True
        out.append(json.dumps(q, ensure_ascii=False))
    open(p, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(p, len(out))
