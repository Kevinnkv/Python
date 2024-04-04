# LỚP SỐ PHỨC

class Solve:
    def __init__(self,a ,b):
        self.a = a
        self.b = b
        
for _ in range (int(input())):
    a1, b1, a2, b2 = map(int, input().split())
    A = complex(a1, b1)
    B = complex(a2, b2)
    s = A + B
    C = s * A
    D = s * s
    C1 = str(int(C.real)) + ' + ' + str(int(C.imag)) + 'i'
    D1 = str(int(D.real)) + ' + ' + str(int(D.imag)) + 'i'
    if C.imag < 0:
        C1 = str(int(C.real)) + ' - ' + str(abs(int(C.imag))) + 'i'
    if D.imag < 0:
        D1 = str(int(D.real)) + ' - ' + str(abs(int(D.imag))) + 'i'
    print(f"{C1}, {D1}")