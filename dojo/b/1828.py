import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(sys.stdin.readline().split()[0])
    p = [int(i) for i in sys.stdin.readline().split()]
    a = [abs(p[i] - (i + 1)) for i in range(n)]
    res = math.gcd(a[0], a[1])
    for i in range(1, len(a)):
        res = math.gcd(res, a[i])
    print(res)
    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    