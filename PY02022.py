# LIỆT KÊ SỐ NGUYÊN TỐ TRONG DÃY

from itertools import count


n = int(input())
list = [int(x) for x in input().split()]
def isPrinme(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
a = []
for i in list:
    if isPrinme(i) and i not in a:
        a.append(i)   
        print(i, list.count(i))


