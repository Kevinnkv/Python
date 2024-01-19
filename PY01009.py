#Chu hoa - chu thuong

s = input()
upper = 0
for i in s:
    if i.isupper():
        upper += 1
if upper > len(s) - upper:
    print(s.upper())
else:
    print(s.lower())
    