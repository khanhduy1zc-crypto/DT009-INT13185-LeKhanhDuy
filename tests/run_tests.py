"""Run 16 DISTINCT test scenarios (15 valid + 1 invalid), check 3 algorithms.
Use no pytest dependencies; each case is counted once even with multiple assertions.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.pair_count import (dem_cap, dem_cap_sau_sap_xep,
                            dem_cap_hai_con_tro, liet_ke_cap, validate_input)
from tests.cases import CASES, INVALID


def run():
    failed = 0
    checks = 0
    for case_id, arr, target, expected, purpose in CASES:
        actuals = [dem_cap(arr, target), dem_cap_sau_sap_xep(arr, target),
                   dem_cap_hai_con_tro(arr, target)]
        checks += 3
        ok = actuals == [expected] * 3
        if len(arr) <= 10:
            pairs = liet_ke_cap(arr, target)
            checks += 2
            ok = ok and len(pairs) == expected and all(1 <= i < j <= len(arr) and arr[i-1] + arr[j-1] == target for i,j in pairs)
            # A pair can never occur twice in output.
            checks += 1
            ok = ok and len(pairs) == len(set(pairs))
        if not ok: failed += 1
        print(f"{case_id:7} {'PASS' if ok else 'FAIL'}  n={len(arr):4} X={target:8} expected={expected:5} actual={actuals} - {purpose}")
    case_id, arr, target, purpose = INVALID
    rejected = False
    try:
        validate_input(arr, target)
    except (TypeError, ValueError) as e:
        rejected = True
        print(f"{case_id:7} PASS  rejected: {e} - {purpose}")
    else:
        print(f"{case_id:7} FAIL  invalid input incorrectly accepted")
    checks += 1
    if not rejected: failed += 1
    n_cases = len(CASES) + 1
    print("=" * 90)
    print(f"SO CA DOC LAP: {n_cases} | PASS: {n_cases-failed} | FAIL: {failed} | SO PHEP KIEM: {checks}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(run())
