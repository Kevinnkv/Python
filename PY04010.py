# LỚP THÍ SINH - 1

class ThiSinh:
    tong_diem = 0
    def __init__(self, ten, ngay_sinh, d1, d2, d3):
        self.ten = ten
        self.ngay_sinh = ngay_sinh
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.tong_diem = d1 + d2 + d3
    # def chuan_hoa(self):
    #     if self.ngay_sinh[1] == '/':
    #         self.ngay_sinh = '0' + self.ngay_sinh[::1]
    #     if self.ngay_sinh[4] == '/':
    #         self.ngay_sinh = self.ngay_sinh[::3] + '/' + self.ngay_sinh[3::]
    #     return self.ngay_sinh
    def __str__(self):
        res = self.ten + " " + self.ngay_sinh + " " + str(self.tong_diem)
        return res
name = input()
ngay_sinh = input()
d1 = float(input())
d2 = float(input())
d3 = float(input())
t = ThiSinh(name,ngay_sinh,d1,d2,d3)
print(t)