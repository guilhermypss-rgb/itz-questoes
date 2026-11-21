# Atualiza o site publicado: gera banco, copia para docs e envia ao GitHub.
python tools/build.py
if (Test-Path docs) { Remove-Item docs -Recurse -Force }
Copy-Item site docs -Recurse
git add -A
git commit -m "Atualiza questoes" 
git push
