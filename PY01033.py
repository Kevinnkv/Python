#BỘ BA NGUYÊN TỐ CÙNG NHAU

import math
def Solve(a,b,c):
    if math.gcd(a,b) == 1 and math.gcd(a,c) == 1 and math.gcd(b,c) == 1:
        return True
    return False

s = input().split()
L = int(s[0])
R = int(s[1])
for i in range(L,R-1):
    for j in range(i+1,R):
        for k in range(j+1,R+1):
            if Solve(i,j,k):
                print('({}, {}, {})'.format(i,j,k))

