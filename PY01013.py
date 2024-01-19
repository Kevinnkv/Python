#ƯỚC SỐ CHUNG NGUYÊN TỐ

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True
def check(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    if isPrime(sum):
        return True
    return False

for i in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        if check(a):
            print("YES")    
        else:
            print("NO")     
    else:
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        if check(a):  
            print("YES")
        else:
            print("NO")
