# ESTADO ATUAL – itz (atualizado 2026-11-21)

## Objetivo
Banco de 20.000 questões inéditas estilo FSADU (Prefeitura de Imperatriz-MA; cargos RAD, FIS, PSI, GMI, TRA) e site de estudos estático publicado de graça.

## Concluído
- Edital 2019 lido (`C:\Users\guilh\Documents\concursos\ITZ\edital itz.pdf`; texto em `fonte/edital.txt`). Tópicos em `data/topics.py`.
- Ferramentas: `tools/validate.py`, `tools/shuffle.py`, `tools/build.py`; regras dos agentes em `BRIEF.md`.
- 710 questões válidas em `lotes/*.jsonl` (meta 20.000 = 3,5%). Revisão independente de ~495: 0 erros de gabarito/fato.
- Site em `site/` (cópia em `docs/`), testado em viewport de celular. Publicado: https://guilhermypss-rgb.github.io/itz-questoes/ (repo guilhermypss-rgb/itz-questoes, GitHub Pages em /docs).
- `RELATORIO.md`, `README.md` (passo a passo de atualização), `HANDOFF.md`, `deploy.ps1`.

## Arquivos alterados/criados
`BRIEF.md`, `data/topics.py`, `tools/*.py`, `site/index.html`, `docs/`, `lotes/`, `RELATORIO.md`, `README.md`, `HANDOFF.md`, `deploy.ps1`, `.gitignore`.

## Decisões
- GMI e Agente de Trânsito não constam no edital 2019: tópicos inferidos da skill. Simulado usa a estrutura de 2019 (`ESTR` em `site/index.html`).
- HG só com fonte oficial verificada (30 questões; faltou fonte das Leis 1.346/2010 e 1.738/2018 e de clima/vegetação).
- GMI-P2 rebaixada para confiança "media" (artigos de memória).
- Geração em lotes de ~40-45 por agente; limite de uso de 5h interrompeu a rodada 2.

## Erros e pendências
- Faltam ~19.290 questões. Lotes não rodados: LP-P3, MAT-P3, HG-P2, RAD-P3, FIS-P3, PSI-P3, GMI-P3, TRA-P2, TRA-P3.
- Vício de tamanho: resposta certa é a mais longa em 48% das "unica" (alvo ~20-30%); só RAD-P2 foi corrigido.
- Não revisados: INF-P2, INF-P3, FIS-P1, RAD-P1, PSI-P1.
- Conferir de memória: RAD-P2-039, PSI-P2 (Leis 10.216 e 13.146), INF.
- Aguardando decisão do usuário: continuar gerando ou corrigir o vício de tamanho primeiro.

## Próxima ação exata
Com a resposta do usuário: lançar agentes (lotes novos, prefixo P3/P4) conforme `BRIEF.md`; depois `python tools/validate.py lotes/*.jsonl` e `powershell -File deploy.ps1`.
