# MA TRẬN - 2

n = int(input())
sumUp = 0
sumDown = 0
for i in range(1,n+1):
    a = [int(x) for x in input().split()]
    for j in range(1,n+1):
        if j < (n-i+1):
            sumUp += a[j-1]
        elif j > (n-i+1):
            sumDown += a[j-1]
diff = abs(sumUp - sumDown)
k = int(input())
if diff <= k:
    print("YES")
else: 
    print("NO")
print(diff)