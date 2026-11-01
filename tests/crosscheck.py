"""Extra correctness checks: independent one-pass frequency oracle (stdlib only)."""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.pair_count import dem_cap, dem_cap_sau_sap_xep, dem_cap_hai_con_tro


def oracle(arr,x):
    seen={}
    count=0
    for value in arr:
        count+=seen.get(x-value,0)
        seen[value]=seen.get(value,0)+1
    return count

rng=random.Random(20261025)
for test_i in range(500):
    length=rng.randrange(0,31)
    a=[rng.randint(-25,25) for _ in range(length)]
    x=rng.randint(-50,50)
    expected=oracle(a,x)
    actual=(dem_cap(a,x),dem_cap_sau_sap_xep(a,x),dem_cap_hai_con_tro(a,x))
    if any(v!=expected for v in actual):
        raise AssertionError((test_i,a,x,expected,actual))
print("RANDOM ORACLE: 500/500 PASS (seed=20261025; not counted as 500 main test cases)")
n=2000
a=[0]*n
x=0
expected=n*(n-1)//2
assert expected==1999000
assert (dem_cap(a,x),dem_cap_sau_sap_xep(a,x),dem_cap_hai_con_tro(a,x))==(expected,)*3
print("BOUNDARY n=2000, a all zeros, X=0: 1999000 pairs; 3/3 algorithms PASS")
