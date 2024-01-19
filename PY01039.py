# Kiểm tra số đẹp

for _ in range (int(input())):
    s = input()
    check = 1
    for i in range(len(s)-2):
        if int(s[i]) != int(s[i+2]):
            check = 0
            break
    if check == 1:
        print("YES")
    else:
        print("NO")
