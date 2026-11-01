# DT009 – Đếm tất cả cặp chỉ số có tổng bằng X

**Sinh viên:** Lê Khánh Duy  
**MSSV:** N24DCDT020  
**Lớp:** D24CQDT01-N  
**Học phần:** INT13185, Nhóm 03  
**Giảng viên:** Hồ Nhựt Minh

## Bài toán

Cho mảng số nguyên `a` và số nguyên `X`. Đếm số cặp chỉ số `i < j` thỏa `a[i] + a[j] == X`. Mỗi vị trí trong mảng được xét độc lập, kể cả khi có các phần tử bằng nhau. Khi `n <= 10`, liệt kê các cặp chỉ số tính từ 1.

Giới hạn đầu vào: `0 <= n <= 2000`, `abs(a[i]) <= 1_000_000`, `abs(X) <= 2_000_000`.

## Môi trường

Python 3.10 trở lên; không cần cài thêm thư viện ngoài.

## Cách chạy

Mở PowerShell trong thư mục chứa `main.py`:

```powershell
python main.py --case VD01 --trace
python main.py --case VD02
python main.py --case TK01
python main.py --case TK02
python main.py --case BIEN01
python main.py --case BIEN02
python main.py --case BIEN03
python main.py --case LOI01
python main.py --array "1,2,2,3" --x 4
python main.py --interactive
python tests/run_tests.py
python tests/crosscheck.py
python tests/verify_components.py
python scripts/benchmark.py
```

`LOI01` sử dụng dữ liệu không hợp lệ để kiểm tra khả năng từ chối đầu vào, nên chương trình thoát với mã 2. Với Windows nếu `python` không có trong PATH, có thể dùng `py -3`.

## Thuật toán

- `dem_cap(a, x)`: duyệt mọi cặp chỉ số, thời gian `O(n²)` và bộ nhớ phụ `O(1)`.
- `liet_ke_cap(a, x)`: liệt kê cặp chỉ số 1-based khi `n <= 10`.
- `merge_sort`, `lower_bound`, `upper_bound`, `dem_cap_sau_sap_xep`: thuật toán sắp xếp và tìm kiếm phần bù tự cài, `O(n log n)` thời gian và `O(n)` bộ nhớ phụ.
- `dem_cap_hai_con_tro`: đối chiếu bằng hai con trỏ và xử lý tần suất trùng.

## Cấu trúc

- `src/pair_count.py`: hàm thuật toán và kiểm tra đầu vào.
- `main.py`: chương trình chạy bằng dòng lệnh.
- `tests/cases.py`: 16 bộ dữ liệu kiểm thử độc lập.
- `tests/run_tests.py`: bộ kiểm thử đầu vào, cặp chỉ số và đối chiếu thuật toán.
- `tests/crosscheck.py`: kiểm chứng bổ sung bằng dữ liệu ngẫu nhiên.
- `tests/verify_components.py`: kiểm thử tính đúng của phép tìm biên, các mảng nhỏ và validator.
- `scripts/benchmark.py`: khảo sát thời gian với `n = 5, 20, 100, 500`.
- `docs/anh_ket_qua`: ảnh chụp minh chứng theo mã A01–A11.
- `docs/log`: kết quả chạy và khảo sát.
- `docs/bao_cao`: báo cáo Word và PDF.

Các lệnh chạy không yêu cầu dữ liệu ngoài; dữ liệu thử nằm trong `tests/cases.py`.
