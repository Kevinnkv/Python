# KIỂM TRA CHIA HẾT
# TLE - Time Limit Exceeded
def prime_sieve(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= N:
        if is_prime[p]:
            for i in range(p * p, N + 1, p):
                is_prime[i] = False
        p += 1
    return [i for i in range(2, N + 1) if is_prime[i]]

def count_numbers(L, R, primes):
    count = 0
    for num in range(L, R + 1):
        divisible = False
        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                divisible = True
                break
        if not divisible:
            count += 1
    return count

if __name__ == "__main__":
    while True:
        a = input().split()
        if len(a) < 2:
            break
        N = int(input())
        primes = prime_sieve(N)
        result = count_numbers(int(a[0]), int(a[1]), primes)
        print(result)

