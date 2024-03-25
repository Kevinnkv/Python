# LỚP PHÂN SỐ - 2

from math import gcd

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def toi_gian(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
    def tong(self, diff):
        self.tu = self.tu * diff.mau + self.mau * diff.tu
        self.mau = self.mau*diff.mau
    def __str__(self):
        return f'{self.tu}/{self.mau}'
if __name__ == '__main__':
    input = input().split()
    p = PhanSo(int(input[0]),int(input[1]))
    q = PhanSo(int(input[2]),int(input[3]))
    p.tong(q)
    p.toi_gian()
    print(p)
    