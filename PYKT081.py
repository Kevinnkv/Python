# Địa chỉ IP

def check_ip(a):
    if len(a) != 4:
        return False
    for i in a:
        if not i.isdigit() or int(i) < 0 or int(i) > 255:
            return False
    return True
for _ in range(int(input())):
    a = [x for x in input().split('.')]
    if check_ip(a):
        print('YES')
    else:
        print('NO')