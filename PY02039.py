# MA TRẬN - 1

n = int(input())
sumUp = 0
sumDown = 0
for i in range(1,n+1):
    a = [int(x) for x in input().split()]
    for j in range(1,n+1):
        if j > i:
            sumUp += a[j-1]
        elif j < i:
            sumDown += a[j-1]
diff = abs(sumUp - sumDown)
k = int(input())
if diff <= k:
    print("YES")
else: 
    print("NO")
print(diff)