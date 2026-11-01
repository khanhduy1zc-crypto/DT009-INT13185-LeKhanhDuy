"""DT009 - Count INDEX pairs i<j with a[i]+a[j]==X (indices 1-based in output).
Self-implemented core: brute force, merge sort, binary lower/upper bounds.
"""
from __future__ import annotations

MAX_N = 2000
MAX_ABS_ELEMENT = 1_000_000
MAX_ABS_X = 2_000_000


def validate_input(a: list[int], x: int) -> None:
    """Raise TypeError/ValueError for invalid input according to DT009."""
    if not isinstance(a, list):
        raise TypeError("a phai la danh sach cac so nguyen")
    if len(a) > MAX_N:
        raise ValueError("So phan tu n phai nam trong [0, 2000]")
    if type(x) is not int:
        raise TypeError("X phai la so nguyen")
    if not -MAX_ABS_X <= x <= MAX_ABS_X:
        raise ValueError("|X| khong duoc vuot qua 2000000")
    for i, value in enumerate(a, start=1):
        if type(value) is not int:
            raise TypeError(f"a[{i}] phai la so nguyen")
        if not -MAX_ABS_ELEMENT <= value <= MAX_ABS_ELEMENT:
            raise ValueError(f"|a[{i}]| khong duoc vuot qua 1000000")


def dem_cap(a: list[int], x: int) -> int:
    """O(n^2) time, O(1) auxiliary memory, no repeated index pairs."""
    validate_input(a, x)
    count = 0
    n = len(a)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] + a[j] == x:
                count += 1
    return count


def liet_ke_cap(a: list[int], x: int) -> list[tuple[int, int]]:
    """List index pairs for n<=10 only; output indices are 1-based."""
    validate_input(a, x)
    if len(a) > 10:
        raise ValueError("Chi liet ke chi so khi n <= 10")
    pairs = []
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == x:
                pairs.append((i + 1, j + 1))
    return pairs


def merge_sort(values: list[int]) -> list[int]:
    """Stable self-implemented merge sort; no use of built-in sorted()."""
    n = len(values)
    if n < 2:
        return values.copy()
    middle = n // 2
    left, right = merge_sort(values[:middle]), merge_sort(values[middle:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:]); merged.extend(right[j:])
    return merged


def lower_bound(values: list[int], value: int, left: int = 0) -> int:
    """First index >= value in the sorted suffix [left, len(values))."""
    lo, hi = left, len(values)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if values[mid] < value:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(values: list[int], value: int, left: int = 0) -> int:
    """First index > value in the sorted suffix [left, len(values))."""
    lo, hi = left, len(values)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if values[mid] <= value:
            lo = mid + 1
        else:
            hi = mid
    return lo


def dem_cap_sau_sap_xep(a: list[int], x: int) -> int:
    """O(n log n) time, O(n) auxiliary memory; correctly handles duplicates."""
    validate_input(a, x)
    ordered = merge_sort(a)
    count = 0
    for i in range(len(ordered) - 1):
        need = x - ordered[i]
        l = lower_bound(ordered, need, i + 1)
        r = upper_bound(ordered, need, i + 1)
        count += r - l
    return count


def dem_cap_hai_con_tro(a: list[int], x: int) -> int:
    """Optional: O(n log n) including sort, O(n) auxiliary memory."""
    validate_input(a, x)
    ordered = merge_sort(a)
    lo, hi, count = 0, len(ordered) - 1, 0
    while lo < hi:
        s = ordered[lo] + ordered[hi]
        if s < x:
            lo += 1
        elif s > x:
            hi -= 1
        elif ordered[lo] == ordered[hi]:
            length = hi - lo + 1
            count += length * (length - 1) // 2
            break
        else:
            left_value, right_value = ordered[lo], ordered[hi]
            c_left = c_right = 0
            while lo <= hi and ordered[lo] == left_value:
                lo += 1; c_left += 1
            while lo <= hi and ordered[hi] == right_value:
                hi -= 1; c_right += 1
            count += c_left * c_right
    return count


def trace(a: list[int], x: int) -> list[tuple[int, int, int, bool, int]]:
    """(i,j,sum,match,cumulative_count) for a small valid example."""
    validate_input(a, x)
    if len(a) > 10:
        raise ValueError("Chi truy vet voi n <= 10")
    result, count = [], 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            total = a[i] + a[j]
            match = total == x
            if match:
                count += 1
            result.append((i + 1, j + 1, total, match, count))
    return result
