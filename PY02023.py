# SẮP XẾP THEO TỔNG CHỮ SỐ

def sumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
for i in range(int(input())):
    n = int(input())
    list = [int(x) for x in input().split()]
    list.sort(key = lambda x: (sumOfDigits(x),x))
    print(*list)
        
