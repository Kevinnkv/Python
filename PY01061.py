# ĐẦU CUỐI NGUYÊN TỐ

import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1
def check(s):
    if isPrime(int(s[:3])) and isPrime(int(s[-3:])):
        return 'YES'
    else:
        return 'NO'
for t in range(int(input())):
    print(check(input()))
    