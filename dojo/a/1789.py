import sys
import math
from collections import defaultdict, Counter


def solution():
    n = int(input())
    a = [int(x) for x in input().split()]
    ok = 'NO'
    for i in range(n):
        for j in range(i):
            if math.gcd(a[i], a[j]) <= 2: 
                ok = 'YES'
    print(ok)

    



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()