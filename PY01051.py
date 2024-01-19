#TỔNG CHỮ SỐ THUẬN NGHỊCH

def Check(s):
    sum = 0
    for i in s:
        sum += int(i)
    if str(sum) == str(sum)[::-1] and sum > 9:
        return True
    else:
        return False

for _ in range(int(input())):
    s = input()
    if Check(s):
        print("YES")
    else:
        print("NO")
