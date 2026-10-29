import json, os, zipfile, traceback
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import nbformat
from IPython.display import display
source=Path(__file__).with_name('22-3834-harpreet-singh-26-chart-professional-edition.ipynb')
nb=nbformat.read(source,as_version=4)
os.chdir(source.parent)
ns={'__name__':'__main__','display':display}
errors=[]
for i in range(62,len(nb.cells)):
    cell=nb.cells[i]
    if cell.cell_type!='code': continue
    try: exec(compile(cell.source,f'cell_{i}', 'exec'),ns)
    except Exception as e:
        errors.append((i,str(e)));print(f'FAILED cell {i}: {e}');traceback.print_exc()
output=source.parent/'professional_26_charts'
if errors: raise SystemExit(f'{len(errors)} failed cells: {errors}')
assert len(ns['CHART_REGISTRY'])==26
archive=source.parent/'Harpreet_Singh_26_Charts_Exports.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    z.write(source,source.name)
    for p in output.rglob('*'):
        if p.is_file(): z.write(p,p.relative_to(source.parent))
print('SUCCESS:',archive,'bytes:',archive.stat().st_size)
