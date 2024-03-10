# THỐNG KÊ DỊCH TỄ

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

n, m = map(int, input().split())
a = []
b = [] # ds luu cac vi tri va danh dau
for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(m):
        if a[i][j] == -1:
            b.append((i, j))
cnt = 0
while len(b) > 0:
    i, j = b.pop()
    for k in dxy:
        x, y = i + k[0], j + k[1]
        if 0 <= x < n and 0 <= y < m:
            cnt += a[x][y] 
            a[x][y] = 0
print(cnt)
            
    


