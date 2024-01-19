# Số may mắn - 2

for i in range(int(input())):
    s = input()
    for i in range(len(s)):
        if s[i] != '4' and s[i] != '7':
            print("NO")
            break
    else:    
        print("YES")                        
        
    