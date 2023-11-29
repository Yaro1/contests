import sys
import math
from collections import defaultdict

def solution():
    n = int(sys.stdin.readline().split()[0])
    l = sum(i for i in range(1, n+1))
    result = [1 + n - (l % n)]
    for i in range(2,n+1):
        result.append(i)
    print(*result)



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()