from pathlib import Path
import shutil,json,subprocess,sys,time,hashlib
from datetime import datetime, timezone
R=Path(__file__).resolve().parent.parent
assert '--resume' not in sys.argv, 'Use a fresh replay; historical receipts are retained.'
BUILD=R/'build'/('replay-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ'))
BUILD.mkdir(parents=True,exist_ok=False)
inputs={p.relative_to(R).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'certificates').rglob('*') if p.is_file() and '__pycache__' not in p.parts}
for tag in ['B','T','S']:
 shutil.copytree(R/'certificates'/tag,BUILD/tag)
logs=BUILD/'logs';logs.mkdir(parents=True,exist_ok=True)
records=[]
(BUILD/'inputs-start.json').write_text(json.dumps(inputs,indent=2))
def run(name,args,cwd,expect):
    if any(r['name']==name and r['accepted'] for r in records):
        return
    t=time.time(); p=subprocess.run([sys.executable,*args],cwd=cwd,capture_output=True,text=True)
    (logs/(name+'.log')).write_text(p.stdout+'\nSTDERR\n'+p.stderr)
    ok=p.returncode==0 and expect(p.stdout)
    rec={'name':name,'returncode':p.returncode,'accepted':ok,'seconds':round(time.time()-t,2)}
    records.append(rec); (BUILD/'progress.json').write_text(json.dumps(records,indent=2))
    print(json.dumps(rec),flush=True)
    assert ok,name
run('B-exact',['certE_exact.py','wE3_W090_32_snap.npz','0.0001','0.0872'],BUILD/'B',lambda s:'EXACT-CERTIFIED' in s and 'FAILED' not in s)
run('B-negative',['certE_exact.py','wE3_W090_32_snap.npz','0.0001','0.09'],BUILD/'B',lambda s:'FAILED' in s)
run('S-all-eight',['cert_slices2.py','0.240','37.7'],BUILD/'S',lambda s:s.count('CERTIFIED')==8 and 'FAILED' not in s and 'ERROR' not in s)
run('S-negative',['cert_slice.py','37.975','0.240','0.2282','0.2282','60'],BUILD/'S',lambda s:'FAILED' in s)
run('neck',['cert_riccati.py','N','0.03','0.45','0.2595','45.8318','100000'],BUILD/'S',lambda s:'CERTIFIED' in s and 'FAILED' not in s)
run('neck-negative',['cert_riccati.py','N','0.03','0.45','0.2595','45.84','100000'],BUILD/'S',lambda s:'FAILED' in s)
# Arb T checker: avoids fcheck's explicitly assumed libm 8-ulp error bound.
sys.path.insert(0,str(BUILD/'T'))
import numpy as np
from ctcert import Box
from ctangle import check_theta_arb
for p in sorted((BUILD/'T/barriers').glob('*.npz')):
    z=np.load(p); args=[str(z[k]) for k in ['tau','m1','m2','wstar']]
    box=Box(*args,Lam0=str(z['Lam0']),Ns=int(z['Ns']),Nl=int(z['Nl']))
    out=check_theta_arb(box,z['theta'],str(z['Lam0']),K_s=str(int(float(z['K']))))
    rec={'name':'T-'+str(z['m1']), 'accepted':bool(out[0]),'fails':int(out[1]),'slack_b':str(out[2]),'slack_c':str(out[3])}
    records.append(rec);print(json.dumps(rec),flush=True);assert rec['accepted'] and rec['fails']==0
    if str(z['m1'])=='0.2280':
        bad=z['theta'].copy(); bad[1999,47]-=1e-6
        b=check_theta_arb(box,bad,str(z['Lam0']),K_s=str(int(float(z['K']))))
        records.append({'name':'T-corrupted-node','accepted':not bool(b[0]),'fails':int(b[1])});assert not b[0] and b[1]>0
    (BUILD/'progress.json').write_text(json.dumps(records,indent=2))
assert len([r for r in records if r['name'].startswith('T-') and r['name']!='T-corrupted-node'])==9
unchanged=all(hashlib.sha256((R/p).read_bytes()).hexdigest()==h for p,h in inputs.items())
assert unchanged
receipt={'status':'PASS','records':records,'shipped_inputs_unchanged':unchanged,'full_pde_formalization':False,'original_problem_solved':False}
(BUILD/'receipt.json').write_text(json.dumps(receipt,indent=2))
print('Receipt:',BUILD/'receipt.json')
print('PASS: all B/T/S/N gates and negative controls; this is certificate replay, not a formal PDE proof')
