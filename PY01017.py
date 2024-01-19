# Mã hóa 1

def encode(s):
    pos = 0
    res = ''
    for i in range(pos+1,len(s)):
        if s[i] != s[pos]:
            res += str(i-pos) + s[pos]
            pos = i
    res += str(len(s)-pos) + s[pos]
    print(res)
        
for t in range(int(input())):
    s = input()
    encode(s)
