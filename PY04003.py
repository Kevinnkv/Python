# LỚP PHÂN SỐ - 1

import math
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def toi_gian(self):
        ucln = math.gcd(self.tu , self.mau)
        self.tu //= ucln
        self.mau //= ucln
    def __str__(self):
        return str(self.tu) + "/" + str(self.mau)
if __name__ ==  '__main__':
    tu, mau = map(int, input().split())
    p = PhanSo(tu, mau)
    p.toi_gian()
    print(p)