"""Hand-computed distinct test inputs and expectations. 1 invalid case = 16 independent tests."""
CASES = [
    ("VD01", [1, 2, 2, 3], 4, 2, "Vi du 1 + ca phieu 1: gia tri trung nhung vi tri khac"),
    ("VD02", [2, 2, 2], 4, 3, "Vi du 2 + ca phieu 2: chon 2 trong 3 vi tri"),
    ("KT03", [1, 4], 8, 0, "Ca phieu 3: khong co nghiem"),
    ("KT04", [-2, 0, 2], 0, 1, "Ca phieu 4: co so am"),
    ("BIEN01", [], 0, 0, "Ca phieu 5: mang rong"),
    ("BIEN02", [5], 10, 0, "Ca phieu 5: mang mot phan tu"),
    ("TK01", [7, 7, 7, 7], 14, 6, "Tu thiet ke 1: 4 phan tu trung nhau"),
    ("TK02", [1, 2, 3, 4, 5], 5, 2, "Tu thiet ke 2: hai cap gia tri khac"),
    ("BIEN03", [1000000, 1000000], 2000000, 1, "Bien tren |X| va |a[i]|"),
    ("KT10", [1000000, -1000000], 0, 1, "Hai gia tri bien doi dau"),
    ("KT11", [0, 0, 0, 0, 0], 0, 10, "Gia tri trung bang 0, 5 chon 2"),
    ("KT12", [-5, -1, 2, 6, 8], 1, 2, "Hai cap so am/duong"),
    ("KT13", [4, 4, 4, 4, 4, 4], 8, 15, "Gia tri trung, 6 chon 2"),
    ("KT14", [1, 2, 3, 4], -2000000, 0, "Can duoi X hop le, khong co cap"),
    ("KT15", [1, 1, 2, 2, 3, 3], 4, 5, "Trung nhieu gia tri: 4 cap 1+3 va 1 cap 2+2"),
]
# Invalid test has separate input and expected rejection, not confused with no-solution.
INVALID = ("LOI01", [1, 2, 1000001], 4, "Gia tri a[3] ngoai mien")
