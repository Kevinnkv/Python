# SỐ PHẢN NGUYÊN TỐ NHỎ NHẤT

# Số nguyên dương N được gọi là phản nguyên tố nếu như số lượng ước số của N lớn hơn số lượng ước số của tất cả các số nguyên dương nhỏ hơn N.
# Ví dụ các số phản nguyên tố đầu tiên: 1, 2, 4, 6, 12, 24, …
# Cho số nguyên dương X, hãy tìm số phản nguyên tố bé nhất không nhỏ hơn X.
# Input:
# Dòng đầu ghi số bộ test T (không quá 106)
# Mỗi test ghi số nguyên dương X (1 ≤ X ≤ 107)
# Output:
# Với mỗi test, ghi ra kết quả tính được trên một dòng.

import sys
from bisect import bisect_left

a = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]
t = int(input())
i = 0
for line in sys.stdin:
    n = int(line.strip())  # Lưu ý sử dụng strip để loại bỏ ký tự xuống dòng
    print(a[bisect_left(a, n)])
    i += 1
    if i == t:
        break

