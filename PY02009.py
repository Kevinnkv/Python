# TRÚNG THƯỞNG

for _ in range(int(input())):
    n = int(input())
    dd = {} # dictionary with key - value
    cnt = 0
    while n > 0:
        x = int(input())
        if x in dd:
            dd[x] += 1
        else:
            dd[x] = 1
        cnt = max(cnt, dd[x])
        n -= 1
    ans = 1000
    for i in dd:
        if dd[i] == cnt:
            ans = min(ans, i)
    print(ans)