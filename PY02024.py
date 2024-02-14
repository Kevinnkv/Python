# SẮP XẾP THEO TÍCH CHỮ SỐ

def productOfDigits(n):
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10
    return product
for _ in range(int(input())):
    n = int(input())
    list = [int(x) for x in input().split()]
    list.sort(key = lambda i: (productOfDigits(i),i))
    print(*list)