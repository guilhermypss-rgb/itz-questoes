# Briefing para geradores de questões FSADU (Prefeitura de Imperatriz-MA)

Escreva questões INÉDITAS no estilo da banca FSADU. Tudo em português do Brasil. Não copie provas reais.

## Saída
Arquivo JSONL (uma questão por linha, JSON válido, UTF-8) no caminho que a tarefa indicar. Depois rode:
`python tools/validate.py <arquivo>` e corrija até zerar os erros; por fim `python tools/shuffle.py <arquivo>` (embaralha alternativas; NÃO edite o gabarito depois). Escreva o arquivo com um script Python (json.dumps, ensure_ascii=False) para garantir JSON válido, ou com a ferramenta Write.

## Campos
id (prefixo da tarefa + número de 3-4 dígitos, único), cargos (lista de RAD/FIS/PSI/GMI/TRA), disciplina (sigla: LP, MAT, INF, HG, RAD, FIS, PSI, GMI, TRA), topico (texto exato dado na tarefa), nivel (facil|medio|dificil), formato (unica|afirmativas|vf|associacao|excecao), texto_base (só LP; 150–300 palavras) e texto_id (LP), enunciado, alternativas (EXATAMENTE 5 strings SEM a letra "a)"), gabarito ("A".."E"; antes do shuffle pode ser qualquer um), comentario (por que a certa está certa + erro das erradas importantes; mín. 60 caracteres), fonte (norma/artigo/obra/URL em que o fato se apoia), confianca (alta|media|baixa), calculo (só MAT: expressão Python cujo valor é a resposta; a alternativa certa deve conter esse número; ex.: "1200*0.85").

## Formatos (proporção alvo na tarefa)
- unica: enunciado direto, 5 alternativas de tamanho parecido.
- afirmativas: enunciado = "Analise as afirmativas a seguir.\nI. ...\nII. ...\nIII. ...\nIV. ...\nEstá correto o que se afirma apenas em:" (ou "Estão corretas apenas as afirmativas:"). Alternativas: "I e III.", "II, III e IV." etc., todas diferentes.
- vf: enunciado = "Em relação a [tema], julgue as afirmativas abaixo em Verdadeiras (V) ou Falsas (F).\n( ) afirmação 1.\n( ) afirmação 2.\n( ) afirmação 3.\nA sequência correta é:" (3 ou 4 itens). Alternativas SÓ no formato "V – F – V" com travessão (–) e espaços. Cinco sequências distintas e plausíveis.
- associacao: colunas "I. ... II. ... III." e "A. ... B. ... C." no enunciado; alternativas "I-C, II-B, III-A." etc.
- excecao: "INCORRETA"/"EXCETO" (use pouco).
Sem "todas as alternativas", "nenhuma das anteriores".

## Distratores (misture, sem repetir o mesmo tipo na questão)
absolutos ("exclusivamente", "independentemente", "sempre", "nunca"); inversão de causa/efeito; troca de conceitos vizinhos; detalhe trocado (número, prazo, órgão, lado); função inventada para ferramenta real; afirmação verdadeira que não responde à pergunta. A correta NÃO pode ser sempre a mais longa. Só uma alternativa correta; confira que as erradas são realmente erradas.

## Níveis
30% facil (um conceito), 50% medio (caso/dois conceitos), 20% dificil (texto/caso longo, distratores quase certos).

## Veracidade (regra mais importante)
Nunca invente lei, artigo, número de lei, prazo, valor, data ou dado local. Use só o que você tem certeza ou pesquisou (WebSearch/WebFetch em fonte oficial: planalto.gov.br, gov.br, IBGE, CFM/COFFITO/CFP/CONTER, Portaria 453/98 etc.). Se não tiver certeza, NÃO escreva a questão; se a base for mais fraca, confianca "media" ou "baixa". Redija legislação perto do texto vigente da lei. Questão sem fonte real = proibida.

## Específicas de saúde
Enunciado longo com caso clínico/técnico (paciente, idade, achados) + "Considerando..., assinale a alternativa correta"; alternativas de 20–45 palavras, técnicas. Radiologia: situação-problema do dia a dia do serviço. GMI e Trânsito: legislação com redação próxima da lei vigente.

## Língua Portuguesa
SEMPRE texto_base original (150–300 palavras), gêneros variados (notícia local/regional, opinião, crônica, letra de canção regional original, texto científico curto). Cada texto serve a 6 a 8 questões (mesmo texto_base e texto_id repetidos em cada linha), com perguntas que exigem voltar ao trecho. Cobrir o tópico da tarefa dentro do texto.

## Matemática
Problema do cotidiano. "básico" (GMI/Trânsito/Radiologia) ou "superior" conforme tarefa. Alternativas numéricas em ordem crescente (use "ordenada": true se a ordem importa). SEMPRE preencher "calculo" nas questões de conta e conferi-lo; distratores = erros típicos.

## Informática
Atual: Google Workspace, Windows 11/Copilot, Microsoft 365, DNS/DHCP, segurança, backup, hardware. Não afirme detalhes de interface que você não tem certeza.

## História e Geografia
Só fato com fonte oficial verificada (IBGE, Prefeitura de Imperatriz, Lei Orgânica, leis municipais, Enciclopédia dos Municípios Maranhenses). Pesquise e cite URL/lei em "fonte". Se não achar, gere menos questões e diga quantas faltaram.

## Resposta final do agente
Uma linha: arquivo, quantas questões válidas, quantas pulou e por quê (ex.: sem fonte).
