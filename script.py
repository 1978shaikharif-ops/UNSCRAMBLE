from pathlib import Path
import zipfile
src = Path('output/unscrambler-app')
zip_path = Path('output/word-unscrambler-github-pages.zip')
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in src.rglob('*'):
        if f.is_file():
            z.write(f, arcname=f.relative_to(src.parent))
print(zip_path.resolve())