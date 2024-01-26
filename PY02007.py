# CHIA DƯ CHO 42
n = 10
res = set()
while n > 0:
    s = input()
    x = s.split()
    n -= len(x)
    for i in x:
        res.add(int(i) % 42)
print(len(res))
