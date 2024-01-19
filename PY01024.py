# CHẴN - LẺ

for t in range(int(input())):
    s = input()
    sum = int(s[0])
    check = 1
    for i in range(1, len(s)):
        sum += int(s[i])
        if abs(int(s[i])-int(s[i-1])) != 2:
            check = 0
            break

    # print(sum)
    if check == 1 and sum % 10 == 0:
        print("YES")
    else:
        print("NO")
        
