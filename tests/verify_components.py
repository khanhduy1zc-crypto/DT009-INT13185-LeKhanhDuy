"""Kiểm tra riêng các thành phần, tính bất biến và đầu vào sai."""
import itertools
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.pair_count import (validate_input, dem_cap, liet_ke_cap,
                            merge_sort, lower_bound, upper_bound,
                            dem_cap_sau_sap_xep, dem_cap_hai_con_tro)


def oracle(a, x):
    return sum(a[i] + a[j] == x
               for i in range(len(a)) for j in range(i + 1, len(a)))


def rejects(a, x):
    try:
        validate_input(a, x)
    except (TypeError, ValueError):
        return True
    return False


def run():
    # Các mục tiêu kiểm tra riêng, không cộng vào 16 ca trong tests/cases.py.
    invalid = [
        (None, 0), ((), 0), ([True], 0), ([1.0], 0),
        ([1000001], 0), ([-1000001], 0), ([0], 2000001),
        ([0], -2000001), ([0], True), ([0] * 2001, 0),
    ]
    for a, x in invalid:
        assert rejects(a, x), (a, x)

    binary_checks = 0
    for n in range(0, 12):
        arr = sorted(random.Random(20261101 + n).choices(range(-3,4), k=n))
        assert merge_sort(arr) == arr
        for left in range(n + 1):
            for target in range(-5, 6):
                l = lower_bound(arr, target, left)
                r = upper_bound(arr, target, left)
                assert left <= l <= r <= n
                assert all(v < target for v in arr[left:l])
                assert all(v == target for v in arr[l:r])
                assert all(v > target for v in arr[r:])
                binary_checks += 1

    exhaustive = 0
    for n in range(0, 5):
        for values in itertools.product((-2, -1, 0, 1, 2), repeat=n):
            a = list(values)
            old = a.copy()
            for x in range(-4, 5):
                expected = oracle(a, x)
                assert dem_cap(a, x) == expected
                assert dem_cap_sau_sap_xep(a, x) == expected
                assert dem_cap_hai_con_tro(a, x) == expected
                pairs = liet_ke_cap(a, x)
                assert len(pairs) == expected
                assert len(pairs) == len(set(pairs))
                assert a == old, "Thuat toan da thay doi input"
                exhaustive += 1

    print(f"INVALID INPUT CHECKS: {len(invalid)}/{len(invalid)} PASS")
    print(f"BINARY BOUNDS CHECKS: {binary_checks}/{binary_checks} PASS")
    print(f"EXHAUSTIVE SMALL INPUTS: {exhaustive}/{exhaustive} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
