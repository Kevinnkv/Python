# Số không giảm

for i in range(int(input())):
    s = input()
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            print("NO")
            break
    else:
        print("YES")