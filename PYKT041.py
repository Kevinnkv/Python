# ĐẾM CẶP ĐỒNG XU

n = int(input())
a = [input() for _ in range(n)]
res = 0
for i in range(n):
    # row
    r = 0
    # column
    c = 0
    for j in range(n):
        if a[i][j] == 'C':
            r += 1
        if a[j][i] == 'C':
            c += 1
    res += r*(r-1)//2 + c*(c-1)//2
print(res)
