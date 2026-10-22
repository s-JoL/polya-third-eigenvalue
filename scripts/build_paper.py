"""Build the article from its LaTeX source using an installed Tectonic."""
from pathlib import Path
import hashlib, json, shutil, subprocess

R=Path(__file__).resolve().parent.parent
source=R/'paper/third-eigenvalue'
build=R/'build/paper'
build.mkdir(parents=True,exist_ok=True)
engine=shutil.which('tectonic')
if engine is None:
    raise SystemExit('Install Tectonic, then run python scripts/build_paper.py again.')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
inputs={p.name:sha(p) for p in source.glob('*.tex')}
cmd=[engine,'--keep-logs','--keep-intermediates','--outdir',str(build),'main.tex']
cp=subprocess.run(cmd,cwd=source,text=True,capture_output=True)
(build/'compile.log').write_text(cp.stdout+cp.stderr)
print(cp.stdout+cp.stderr)
assert cp.returncode==0, 'LaTeX compilation failed; see build/paper/compile.log'
log=(build/'main.log').read_text()
assert not any(s in log for s in ['Overfull','undefined references','undefined citations','! LaTeX Error'])
assert inputs=={p.name:sha(p) for p in source.glob('*.tex')}
shutil.copy2(build/'main.pdf',source/'paper.pdf')
receipt={'status':'PASS','source_hashes':inputs,'pdf_sha256':sha(source/'paper.pdf'),'compiler':subprocess.check_output([engine,'--version'],text=True).strip(),'no_overfull_boxes_or_unresolved_references':True}
(build/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('PDF:',source/'paper.pdf')
