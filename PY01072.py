# BÀI TOÁN TỔ HỢP

import itertools

n, k = map(int, input().split())
a = list(map(int, input().split()))
arr = list(set(a))
arr.sort()
res = list(itertools.combinations(arr, k))

for i in res:
    print(*i)
