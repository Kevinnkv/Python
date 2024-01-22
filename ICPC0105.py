# Tìm số lớn nhất

for t in range(int(input())):
    s = input()
    res = 0
    number = ''
    for i in s:
        if i.isdigit():
            number += i
        else:
            if number:
                res = max(res, int(number))
                number = ''

    if number:
        res = max(res, int(number)) 
    print(res)
    