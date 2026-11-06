"""Parse sources and notebook JSON without executing research code."""
import ast
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
count = 0
for path in sorted(root.rglob('*')):
    if any(part.startswith('.') or part in {'data', 'outputs', '__pycache__'} for part in path.relative_to(root).parts):
        continue
    if path.suffix == '.py':
        ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
        count += 1
    elif path.suffix in {'.json', '.ipynb'}:
        obj = json.loads(path.read_text(encoding='utf-8'))
        if path.suffix == '.ipynb':
            assert obj['nbformat'] == 4
            for index, cell in enumerate(obj['cells']):
                if cell['cell_type'] == 'code':
                    assert cell.get('outputs') == [], (path, index, 'outputs')
                    assert cell.get('execution_count') is None, (path, index, 'execution_count')
                    ast.parse(''.join(cell['source']), filename=f'{path}:cell {index + 1}')
        count += 1
print(f'Parsed {count} source/JSON files; no research code executed.')
