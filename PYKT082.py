# TÍNH ĐIỂM THI IELTS

def getScores(s):
    if 39 <= s <= 40:
        return 9.0
    elif 37 <= s <= 38:
        return 8.5
    elif 35 <= s <= 36:
        return 8.0
    elif 33 <= s <= 34:
        return 7.5
    elif 30 <= s <= 32:
        return 7.0
    elif 27 <= s <= 29:
        return 6.5
    elif 23 <= s <= 26:
        return 6.0
    elif 20 <= s <= 22:
        return 5.5
    elif 16 <= s <= 19:
        return 5.0
    elif 13 <= s <= 15:
        return 4.5
    elif 10 <= s <= 12:
        return 4.0
    elif 7 <= s <= 9:
        return 3.5
    elif 5 <= s <= 6:
        return 3.0
    else:
        return 2.5
def round(s):
    if s - int(s) >= 0.5:
        return int(s) + 1.0
    elif 0.25 <= s - int(s) <= 0.5:
        return int(s) + 0.5
    else:
        return int(s)
for _ in range(int(input())):
    a = input().split()
    overall = round((getScores(int(a[0])) + getScores(int(a[1])) + float(a[2]) + float(a[3])) / 4.0)
    print("{:.1f}".format(overall))
    # print(overrall)