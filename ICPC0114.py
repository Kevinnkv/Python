#PERFECT PRIME

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
def check(n):
    n = str(n)
    sum = 0
    if isPrime(int(n)) and isPrime(int(n[::-1])):
        for i in range(len(n)):
            if n[i] not in ['2', '3', '5', '7']:
                return False
            else:
                sum += int(n[i])
        if isPrime(sum):
            return True
    return False
        
for _ in range(int(input())):
    n = int(input())
    if check(n):
        print("Yes")
    else:
        print("No")
    