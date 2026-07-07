from pathlib import Path
p = Path('output/word-unscrambler-github-pages.zip')
print(p.exists(), p.stat().st_size)