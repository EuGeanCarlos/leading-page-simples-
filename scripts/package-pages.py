"""Empacota apenas os recursos públicos versionados do projeto original."""
from pathlib import Path
import shutil
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'leading page 01'
FILES = ['css/style.css', 'imagens/arrow.png', 'imagens/bg-form.jpg', 'imagens/logo1.png', 'imagens/logo2.png', 'imagens/mosaico1.jpg', 'imagens/mosaico2.jpg', 'imagens/mosaico3.jpg', 'imagens/mosaico4.jpg', 'index.html']
DEST = ROOT / "_site"
DEST.mkdir(exist_ok=True)
for name in FILES:
    target = DEST / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE / name, target)
assert (DEST / "index.html").is_file(), "Entrada index.html ausente"
(DEST / ".nojekyll").touch()
