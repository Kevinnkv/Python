#NGUYÊN TỐ CÙNG NHAU

import math
def Solve(a,b):
    if math.gcd(a,b) == 1:
        return True
    return False
s = input().split()
n = int(s[0])
k = int(s[1])
cnt = 0
for i in range(10**(k-1),10**k):
    if Solve(n,i):
        cnt += 1
        print(i,end=' ')
    if cnt == 10:
        print()
        cnt = 0
    