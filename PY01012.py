# Chèn xâu
# cach 1
# s1 = input()
# s2 = input()
# index = int(input()) - 1
# print(s1[:index] + s2 + s1[index:])
# cach 2
# s1 = list(input())
# s2 = input()
# index = int(input()) - 1
# s1.insert(index, s2)
# print(''.join(s1))
# cach 3
s1 = input()
s2 = input()
index = int(input()) - 1
for i in range(0,index):
    print(s1[i], end = '')
print(s2, end = '')
for i in range(index, len(s1)):
    print(s1[i], end = '')