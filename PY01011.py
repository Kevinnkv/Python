# Liệt kê số đẹp
# Cho số nguyên dương N, hãy liệt kê các số thuận nghịch nhỏ hơn N thỏa mãn điều kiện:
# Chỉ có các chữ số 0,2,4,6,8
# Số chữ số của N chia cho 2 dư 1
# Input
# Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 < N <106)
# Output
# Ghi kết quả của mỗi test trên một dòng, mỗi số cách nhau đúng một khoảng trống.

def is_beautiful_number(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    for i in s:
        if int(i) % 2 != 0:
            return False
    return s == s[::-1]

for i in range(int(input())):
    n = int(input())
    for j in range(22, n):
        if is_beautiful_number(j):
            print(j, end=" ")
    print()

    