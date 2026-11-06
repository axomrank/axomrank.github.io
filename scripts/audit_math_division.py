"""List every // in the maths lessons that dropped a remainder, so a person can check it.

A right answer must never appear here. Distractors and the middle of an odd count may.
Run from the repo root: python3 scripts/audit_math_division.py
"""
import ast, sys, pathlib, re
root = pathlib.Path('scripts/math_course')
class Exact(int):
    pass
bad = set()
class Tr(ast.NodeTransformer):
    def visit_BinOp(self, n):
        self.generic_visit(n)
        if isinstance(n.op, ast.FloorDiv):
            return ast.Call(ast.Name('_fd', ast.Load()), [n.left, n.right, ast.Constant(n.lineno)], [])
        return n
sys.path.insert(0, 'scripts/math_course')
import math_kit
def _fd(a, b, line):
    if a % b: bad.add((CUR, line))
    return a // b
for f in sorted(p.stem for p in root.glob('math_lessons_*.py')):
    CUR = f
    src = (root / f'{f}.py').read_text(encoding='utf-8')
    tree = ast.fix_missing_locations(Tr().visit(ast.parse(src)))
    g = {'_fd': _fd, '__name__': f}
    exec(compile(tree, f, 'exec'), g)
    for name, fn in list(g.items()):
        if re.fullmatch(r'l\d+', name): fn()
lines = {}
for f, l in sorted(bad):
    t = (root / f'{f}.py').read_text(encoding='utf-8').split('\n')[l-1]
    lines.setdefault(f, []).append((l, t.strip()[:170]))
for f, v in lines.items():
    print('==', f)
    for l, t in v: print(l, t)
print('inexact sites', len(bad))
