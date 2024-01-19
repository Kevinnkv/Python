#Số phát lộc

for i in range(int(input())):
    s = input()
    if s[len(s)-2] == '8' and s[len(s)-1] == '6':
        print("YES")
    else:
        print("NO")
        