# KIỂM TRA CHIA HẾT
# TLE - Time Limit Exceeded
def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    input_str = input()
    if input_str == "-1":
        break

    a, b = map(int, input_str.split())
    n = int(input())
    count = 0

    for i in range(a, b + 1):
        if is_prime(i) and i % n == 0:
            count += 1

    print(count)
