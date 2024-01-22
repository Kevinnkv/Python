# Xoay Mảng

for _ in range(int(input())):
    n, index = map(int, input().split())
    s = input().split()
    res = s[index:] + s[:index]
    print(*res)