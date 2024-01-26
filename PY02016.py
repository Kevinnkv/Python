# XUẤT HIỆN NHIỀU LẦN NHẤT

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max = 0
    for i in d:
        if d[i] > max:
            max = d[i]
    if max > n//2:
        for i in d:
            if d[i] == max:
                print(i)
                break
    else:
        print("NO")