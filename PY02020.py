# TÍNH ĐIỂM TRUNG BÌNH

n = int(input())
a = [float(x) for x in input().split()]
b = sorted(a)
sum = 0
cnt = 0
for i in range(n):
    if a[i] != b[n-1] and a[i] != b[0]:
        sum += a[i]
        cnt += 1
print(round(sum/cnt,2))

