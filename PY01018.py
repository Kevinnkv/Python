# Mã hóa 2
# Cho dãy ký tự chuẩn P[] gồm 28 chữ cái, trong đó có 26 chữ cái in hoa từ A đến Z, hai ký tự cuối là gạch dưới ‘_’ và dấu chấm ‘.’
# P[] = “ABCDEFGHIJKLMNOPQRSTUVWXYZ_.”
# Phép mã hóa với khoảng cách K (0<K<28) được định nghĩa là phép chuyển các ký tự s[i] thành ký tự P[(i+K)%28] trong dãy ký tự chuẩn P nói trên.
# Ví dụ với K = 3 thì ‘A’ chuyển thành ‘D’; ‘B’ chuyển thành ‘E’ và ‘.’ chuyển thành ‘C’.
# Cho số K và một xâu S (chỉ bao gồm các chữ cái thuộc P[], không có khoảng trống). Hãy mã hóa xâu S theo quy tắc trên, sau đó đảo ngược thứ tự các chữ cái.
# Input
# Mỗi dòng ghi số K và xâu S.
# Input kết thúc khi K = 0.
# Output
# Ghi ra kết quả cho từng test.
def encode(k, s):
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    k = int(k)
    s = str(s)
    result = ""
    for i in range(0, len(s)):
        result += P[(P.find(s[i]) + k)%28] 
    return result[::-1]

while True:
    ls = [str(i) for i in input().split()]
    if len(ls) == 1:
        break
    print(encode(ls[0], ls[1]))

