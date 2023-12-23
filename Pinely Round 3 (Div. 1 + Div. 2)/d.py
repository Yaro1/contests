from sys import stdin
input = lambda: stdin.buffer.readline().decode().strip()
from math import gcd
from functools import reduce


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    
    if a[0] == a[-1]:
        print(0)

    elif a[-1] < k or a[0] > k:
        d = [abs(x - k) for x in a]
        g = reduce(gcd, d)
        print(sum(x//g - 1 for x in d))

    else:
        print(-1)