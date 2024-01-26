#CẶP NGHỊCH THẾ

n = int(input())
list = [int(x) for x in input().split()]
count = 0
for i in range(n-1):
    for j in range(i+1, n):
        if list[i] > list[j]:
            count += 1
print(count)
