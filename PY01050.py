#KÝ TỰ A – B – C
# Hãy liệt kê tất cả các xâu ký tự có độ dài không quá N, chỉ tạo bởi các ký tự A, B, C và thỏa mãn các điều kiện sau:

# Chứa cả ba ký tự A, B, C
# Số ký tự A không nhiều hơn số ký tự B, số ký tự B không nhiều hơn số ký tự C
# Input

# Chỉ có một dòng ghi số N, không quá 12.

# Output

# Ghi ra lần lượt các xâu thỏa mãn theo thứ tự độ dài từ ngắn nhất đến dài nhất.

# Nếu có cùng độ dài thì ghi theo thứ tự từ điển.

# Mỗi xâu ghi trên một dòng.

def Try(str, n, a, b, c):
    # a,b,c là số lượng ký tự A,B,C
    if len(str) == n and 0 < a <= b <= c:
        print(str)
    if len(str) < n:
        Try(str + 'A', n, a + 1, b, c)
        Try(str + 'B', n, a, b + 1, c)
        Try(str + 'C', n, a, b, c + 1)


n = int(input())
for i in range(3, n + 1):
    Try('', i, 0, 0, 0)