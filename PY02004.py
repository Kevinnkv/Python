#DÃY SỐ NHỊ PHÂN
n = int(input())
list = [int(x) for x in input().split()]
count = 0
for i in range(n-1):
    if list[i] != list[i+1]:
        count += 1
print(count)
