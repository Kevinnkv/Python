# SỐ KRISH

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

for _ in range(int(input())):
    n = input()
    sum = 0
    for i in n:
        sum += fact(int(i))                
    if sum == int(n):
        print("Yes")
    else:
        print("No")

