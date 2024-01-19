# TỔNG CHỮ SỐ NGUYÊN TỐ

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
for _ in range(int(input())):
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if isPrime(sum):
        print("YES")
    else:
        print("NO")