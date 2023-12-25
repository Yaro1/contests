import sys
import math
from collections import defaultdict, Counter

def solution():
    n, m = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    b.sort()
    ma = b[-1]
    s = (ma - b[0]) * (max(n, m) - 1) * (min(n, m))
    s += (max(ma - b[1], b[-2] - b[0])) * (min(n, m) - 1)
    print(s)
    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    