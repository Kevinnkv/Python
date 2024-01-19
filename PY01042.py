# KIỂM TRA HỆ CƠ SỐ 3

for _ in range(int(input())):
    s = input()
    check = 1
    for i in range(len(s)):
        if s[i] != '0' and s[i] != '1' and s[i] != '2' :
            check = 0
            break
    if check == 1:
        print("YES")
    else:
        print("NO")