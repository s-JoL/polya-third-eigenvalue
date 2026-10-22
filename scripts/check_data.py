"""Check the geometric and indexing premises of the shipped certificate arrays."""
from pathlib import Path
import json
from fractions import Fraction as F
import numpy as np

R=Path(__file__).resolve().parent.parent
z=np.load(R/'certificates/B/wE3_W090_32_snap.npz',allow_pickle=False)
u,s,w,vid=z['U'],z['S'],z['w'],z['vid']
assert u.ndim==s.ndim==w.ndim==1
assert u[0]==0 and u[-1]==2 and u[int(z['n1'])]==1
assert s[0]==0 and np.all(np.diff(u)>0) and np.all(np.diff(s)>0)
assert all(np.isfinite(x).all() for x in [u,s,w])
assert vid.shape==(len(u),len(u),len(s))
assert np.issubdtype(vid.dtype,np.integer) and vid.min()>=0 and vid.max()<len(w)
assert F(float(z['W']))>=F('0.9') and F(float(z['Lam0']))>=F('37.7')
assert 6*(len(u)-1)**2*(len(s)-1)==8664
ends=['0.03','0.1','0.15','0.19','0.21','0.22','0.225','0.227','0.228','0.2282']
expected={(F(a),F(b)) for a,b in zip(ends,ends[1:])}
seen=set()
for p in (R/'certificates/T/barriers').glob('*.npz'):
    b=np.load(p,allow_pickle=False)
    pair=(F(str(b['m1'])),F(str(b['m2'])))
    assert pair in expected and pair not in seen
    seen.add(pair)
    assert F(str(b['tau']))==F('0.45') and F(str(b['Lam0']))==F('37.7')
    assert F(str(b['wstar']))==F('0.241') and F(str(b['K']))==20
    assert int(b['Ns'])==2000 and int(b['Nl'])==48
    assert b['theta'].shape==(2001,49) and np.isfinite(b['theta']).all()
assert seen==expected
(R/'build').mkdir(exist_ok=True)
receipt={'status':'PASS','B_tetrahedra':8664,'B_grid_and_indices_checked':True,'T_parameter_boxes':9,'T_full_interval_cover_checked':True}
(R/'build/data-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
