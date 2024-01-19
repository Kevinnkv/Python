# Số thuận nghịch chẵn

def Solve(s):
    if s != s[::-1] or len(s) % 2 != 0:
        return False
    else:
        for i in range(len(s)):
            if int(s[i]) % 2 != 0:
                return False
    return True

for _ in range(int(input())):
    s = input()
    for i in range(22,int(s)):
        if Solve(str(i)):
            print(i,end = ' ')

    print()
