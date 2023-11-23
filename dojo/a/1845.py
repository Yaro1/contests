import sys
import math

def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if x != 0]
    return sieve1

def solution():
    n, k, x = map(int, sys.stdin.readline().split())
    if x != 1:
        print("YES")
        print(n)
        print(*([1] * n))
    elif k == 1 or (k == 2 and n % 2 == 1):
        print("NO")
    else:
        print("YES")
        print(n // 2)
        print(*([3 if n % 2 == 1 else 2] + [2] * (n // 2 - 1)))



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()