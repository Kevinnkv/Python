#DÃY SỐ PHÙ HỢP
# 2 3 5 7
# 4 5 7 8
def check(listA, listB):
    for i in range(n):
        if listA[i] > listB[i]:
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    listA = [int(x) for x in input().split()]
    listB = [int(x) for x in input().split()]
    listA.sort()
    listB.sort()
    if check(listA,listB):
        print("YES")
    else:
        print("NO")