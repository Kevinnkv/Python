
#Tìm số nhỏ nhất
for t in range(int(input())):
    s = input()
    res = float('inf')
    number = ''
    for i in s:
        if i.isdigit():
            number += i
        else:
            if number:
                res = min(res, int(number))
                number = ''

    if number:
        res = min(res, int(number)) 
    print(res)
    