#TÍCH CHỮ SỐ - TỔNG CHỮ SỐ

for _ in range(int(input())):
    s = input()
    sum = 0
    product = 1
    cnt = 0
    le = 0
    for i in range(len(s)):
        if i % 2 == 1:
            sum += int(s[i])
        else:
            le += 1
            if s[i] == '0':
                cnt += 1
                continue
            else:
                product *= int(s[i])
    if cnt == le:
        product = 0
    print(product, sum)