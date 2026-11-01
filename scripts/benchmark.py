"""Reproducible benchmarking with warmups and medians, excludes input/output."""
from pathlib import Path
import csv
import json
import platform
import random
import statistics
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.pair_count import dem_cap, dem_cap_sau_sap_xep, dem_cap_hai_con_tro

sizes=(5,20,100,500)
functions=(('hai_vong',dem_cap),('sort_nhi_phan',dem_cap_sau_sap_xep),('hai_con_tro',dem_cap_hai_con_tro))
rows=[]
for n in sizes:
    rng=random.Random(20261025+n)
    a=[rng.randrange(-1000,1001) for _ in range(n)]
    x=17
    expected=dem_cap(a,x)
    for key,fn in functions:
        assert fn(a,x)==expected, (n,key)
        for _ in range(3): fn(a,x)
        times=[]
        for _ in range(15):
            t0=time.perf_counter_ns()
            actual=fn(a,x)
            times.append((time.perf_counter_ns()-t0)/1_000_000)
            assert actual==expected
        row={'n':n,'algorithm':key,'X':x,'expected_pairs':expected,
             'pair_comparisons_brute':n*(n-1)//2,
             'median_ms':round(statistics.median(times),6),
             'min_ms':round(min(times),6),'max_ms':round(max(times),6),'repetitions':len(times)}
        rows.append(row)
        print(f"n={n:4d} | {key:14s} | pairs={expected:3d} | median={row['median_ms']:.6f} ms | min={row['min_ms']:.6f} ms | max={row['max_ms']:.6f} ms")
base=Path(__file__).resolve().parents[1]/'docs'/'log'
base.mkdir(parents=True,exist_ok=True)
with open(base/'khao_sat.csv','w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=rows[0].keys())
    writer.writeheader();writer.writerows(rows)
(base/'khao_sat.json').write_text(json.dumps({'python':sys.version,'platform':platform.platform(),'warmups':3,
    'repetitions':15,'timer':'time.perf_counter_ns','input_generation':'Random(20261025+n), values in [-1000,1000], X=17','rows':rows},indent=2,ensure_ascii=False),encoding='utf-8')
print('KHAO SAT: done; data = docs/log/khao_sat.csv + khao_sat.json')
