# ĐỔI CƠ SỐ

f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(int(input())):
    n, b = map(int, input().split())
    res = ''
    while n > 0:
        res += f[n % b]
        n //= b
    print(res[::-1])
