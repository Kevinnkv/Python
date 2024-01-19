#KIỂM TRA NGUYÊN TỐ

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
for _ in range(int(input())):
    s = input()
    # Lấy 4 ký tự cuối
    l = int(s[-4:]) 
    if isPrime(l):
        print("YES")
    else:
        print("NO")