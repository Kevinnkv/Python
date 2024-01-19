#KIỂM TRA CHIA HẾT CHO 7

for t in range(int(input())):
    s = input()
    check = 1
    sum = int(s)
    for _ in range(1000):
        if  sum % 7 == 0:
            print(sum)
            check = 0
            break
        re_sum = str(sum)[::-1]
        sum += int(re_sum)
    if check == 1:
        print(-1)
