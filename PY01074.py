# Tổng ước số

import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1
def check(n):
    sum1 = 0
    for i in range(2,int(math.sqrt(n))+1):
        count = 0
        if n % i == 0 and isPrime(i):
            while n % i == 0:
                
                count += 1
                n /= i
        sum1 += count*i
    if n > 1:
        sum1 += n
    return sum1
k = int(input())
sum2 = 0
for i in range(k):
    n = int(input())
    sum2 += check(n)
print(int(sum2))

    

