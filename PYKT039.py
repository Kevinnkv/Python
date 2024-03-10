# DÃY SỐ PHÙ HỢP

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    check = 0
    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            check = 1
            break
    if check == 0:
        print("YES")