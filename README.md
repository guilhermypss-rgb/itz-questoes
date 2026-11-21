# Caderno de Provas – Imperatriz

Site de estudos com questões de treino no estilo FSADU.
Link: https://guilhermypss-rgb.github.io/itz-questoes/

## Como atualizar (passo a passo)
1. Coloque os novos arquivos de questões (`.jsonl`) na pasta `lotes`.
2. Abra o PowerShell na pasta do projeto e rode: `python tools/validate.py lotes/*.jsonl` (precisa mostrar `invalidas=0`).
3. Rode: `powershell -File deploy.ps1`. Isso monta o banco, atualiza o site e envia para a internet.
4. Espere cerca de 1 minuto e abra o link. Se não mudar, atualize a página com Ctrl+F5.

Aviso: questões de treino; confira leis e dados locais nas fontes oficiais.
