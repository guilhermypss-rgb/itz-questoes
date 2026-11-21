# HANDOFF – Banco de questões FSADU Imperatriz

## Objetivo
20.000 questões inéditas estilo FSADU + site estático. Cargos: RAD, FIS, PSI, GMI, TRA.

## Estado (verificado)
- Site publicado: https://guilhermypss-rgb.github.io/itz-questoes/ (repo guilhermypss-rgb/itz-questoes, Pages em /docs).
- Banco: ver RELATORIO.md (gerado por `python tools/build.py`). Cerca de 710 questões válidas, 0 inválidas. Meta 20.000: NÃO atingida (~3,5%).
- Revisão independente de ~495 questões: 0 erros de gabarito/fato; 1 ajuste de redação. Não revisados: INF-P2, INF-P3, FIS-P1, RAD-P1, PSI-P1.
- Site testado no viewport de celular (375px): praticar, simulado, desempenho e banco funcionam, sem rolagem horizontal.

## Pendente
- Gerar o restante (~19.300): lotes LP-P3, MAT-P3, HG-P2, RAD-P3, FIS-P3, PSI-P3, GMI-P3, TRA-P2, TRA-P3 estavam planejados e não rodaram (limite de uso). Depois, novos prefixos (P4, P5...) por tópico.
- GMI e Agente de Trânsito NÃO constam no edital 2019 enviado (só Radiologia, Fisioterapia, Psicologia). Tópicos deles foram inferidos da skill. Enviar o edital novo e refazer `data/topics.py` e a estrutura do simulado (`ESTR` em site/index.html).
- HG: faltou fonte para as Leis 1.346/2010 e 1.738/2018 e para clima/vegetação. Não gerar sem fonte.
- Conferir de memória: GMI-P2 (marcadas "media"), RAD-P2-039, PSI-P2 (Leis 10.216 e 13.146), INF-P2/P3.

## Como continuar
1. Ler BRIEF.md (regras dos geradores).
2. Lançar agentes com prompt: tarefa + tópicos exatos + prefixo novo + saída `lotes\<ID>.jsonl`; cada agente roda `python tools/validate.py` e `python tools/shuffle.py`.
3. `powershell -File deploy.ps1` (gera banco, copia para docs, commit e push).

## Arquivos-chave
- C:\Users\guilh\Documents\CLAUDE\itz\BRIEF.md · data\topics.py · tools\validate.py · tools\shuffle.py · tools\build.py · site\index.html · lotes\ · RELATORIO.md · deploy.ps1
- Edital usado: C:\Users\guilh\Documents\concursos\ITZ\edital itz.pdf (Edital 001/2019).
