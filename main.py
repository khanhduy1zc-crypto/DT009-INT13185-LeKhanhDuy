"""DT009: chạy ví dụ, dữ liệu nhập và truy vết thuật toán."""
import argparse
import sys
from src.pair_count import (validate_input, dem_cap, liet_ke_cap,
                            dem_cap_sau_sap_xep, dem_cap_hai_con_tro, trace)
from tests.cases import CASES, INVALID

CASES_BY_ID = {case[0]: case for case in CASES}


def show_case(case_id, arr, x, expected=None, do_trace=False):
    print(f"DT009 | LE KHANH DUY | N24DCDT020 | {case_id}")
    print(f"Input : a={arr}; n={len(arr)}; X={x}")
    try:
        count = dem_cap(arr, x)
        compare = dem_cap_sau_sap_xep(arr, x)
        extra = dem_cap_hai_con_tro(arr, x)
        print(f"Direct (2 loops)        : {count}")
        print(f"Sorted + binary bounds : {compare}")
        print(f"Two pointers (optional): {extra}")
        if len(arr) <= 10:
            print(f"Pairs (1-based, i<j)   : {liet_ke_cap(arr,x)}")
        if expected is not None:
            print(f"Expected                : {expected}")
            success = (count == compare == extra == expected)
            print(f"Result                  : {'PASS' if success else 'FAIL'}")
            if not success:
                return 1
        if do_trace:
            print("TRACE: step | i | j | a[i]+a[j] | match | count")
            for step, (i,j,s,match,count_so_far) in enumerate(trace(arr,x),1):
                print(f"{step:5d} | {i:1d} | {j:1d} | {s:9d} | {'YES' if match else 'NO ':5s} | {count_so_far}")
        return 0
    except (TypeError,ValueError) as exc:
        print(f"INPUT REJECTED: {type(exc).__name__}: {exc}")
        return 2


def main():
    parser=argparse.ArgumentParser(description="DT009 count index pairs i<j with a[i]+a[j]==X")
    parser.add_argument("--case",help="Case id: VD01, VD02, TK01, TK02, BIEN01, BIEN02, BIEN03, LOI01 etc")
    parser.add_argument("--array",help='Comma-separated integers e.g. "1,2,2,3"; use "" for []')
    parser.add_argument("--x",type=int,help="Target X for --array")
    parser.add_argument("--trace",action="store_true",help="Print step-by-step trace for n<=10")
    parser.add_argument("--interactive",action="store_true",help="Read n, array and X from keyboard")
    args=parser.parse_args()
    if args.case:
        case_id = args.case.upper()
        if case_id == "LOI01":
            _,arr,x,_=INVALID
            return show_case(case_id,arr,x)
        if case_id not in CASES_BY_ID:
            parser.error(f"Unknown case id '{case_id}'.")
        _,arr,x,expected,_=CASES_BY_ID[case_id]
        return show_case(case_id,arr,x,expected,args.trace)
    if args.interactive:
        try:
            n=int(input("Nhap n (0..2000): ").strip())
            arr=list(map(int,input("Nhap n so nguyen cach nhau boi dau cach: ").split())) if n else []
            if len(arr)!=n: raise ValueError("So luong phan tu nhap khong khop n")
            x=int(input("Nhap X: ").strip())
            return show_case("NHAP_TAY",arr,x,do_trace=args.trace)
        except ValueError as exc:
            print(f"INPUT REJECTED: {exc}")
            return 2
    if args.array is not None:
        if args.x is None: parser.error("--array requires --x")
        try:
            arr=list(map(int,args.array.split(','))) if args.array.strip() else []
        except ValueError:
            parser.error("--array must contain comma-separated integers")
        return show_case("TU_NHAP",arr,args.x,do_trace=args.trace)
    parser.print_help()
    return 0

if __name__ == '__main__':
    sys.exit(main())
