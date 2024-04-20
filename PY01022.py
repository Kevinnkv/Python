# TỔNG CHỮ SỐ

def sum_digits(s):
    sum = 0
    for i in s:
        sum += ord(i) - ord('0')
    return str(sum)
if __name__ == '__main__':
    s = input()
    cnt = 0
    if len(s) == 1:
        print(1)
    else:
        while len(s) > 1:
            s = sum_digits(s)
            cnt += 1
        print(cnt)