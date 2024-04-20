# TÍNH TỔNG CÁC CHỮ SỐ

def sum_digits(s):
    # Tính tổng các chữ số trong chuỗi s
    sum = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
    return sum
if __name__ == '__main__':
    for i in range(int(input())):
        s = input()
        c = [char for char in s if char.isalpha() ]
        c.sort()
        # print(c)
        # total_sum = int(sum_digits(s))
        print(*c, sum_digits(s), sep = '')