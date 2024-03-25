# LỚP TRIANGLE - 1

# from decimal import Decimal
import math
class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y
    def distance(self, diff): # khoang cach giua self va diff
        a = self.x - diff.x
        b = self.y - diff.y
        d = math.sqrt(a**2+b**2)
        return d
g = []
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(float(arr[0]), float(arr[1]))
        p2 = Point(float(arr[2]), float(arr[3]))
        p3 = Point(float(arr[4]), float(arr[5]))
        e1 = p1.distance(p2)
        e2 = p2.distance(p3)
        e3 = p3.distance(p1)
        a = []
        a.append(e1)
        a.append(e2)
        a.append(e3)
        a.sort()
        # print(a)
        # print(e1, e2, e3)
        if a[0] + a[1] > a[2]:
            sum = a[0] + a[1] + a[2]
            g.append(sum)
            # print(f'{sum:.3f}')
        else:
            print("INVALID")
        t -= 1
    for i in range (len(g)):
        print(f'{g[i]:.3f}')