# ƯU THẾ NGUYÊN TỐ

import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1
def check(s):
    count = 0
    for i in range(len(s)):
        if isPrime(int(s[i])):
            count += 1
    if isPrime(len(s)) and count > len(s) - count:
        return 'YES'
    else:
        return 'NO'
for t in range(int(input())):
    print(check(input()))