# THAY ĐỔI CHỮ SỐ

for _ in range(int(input())):
    p,q =[x for x in input().split()]
    # Nhập x1 ,x2 có thể cùng trên 1 dòng hoặc có nhiều khoảng trắng. Trong bộ test phải nhập thêm 1 dòng cho x2
    s = input().strip()
    if s.count(" ") > 0:
        x1, x2 = s.split()
    else:
        x1 = s
        x2 = input().strip()

    num1 = int(x1.replace(p,q)) + int(x2.replace(p,q))
    num2 = int(x1.replace(q,p)) + int(x2.replace(q,p))
    print(min(num1,num2), max(num1,num2))