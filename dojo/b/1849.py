import sys
import math
from collections import defaultdict, Counter

def solution():
    n, k = map(int, input().split())
    a = list(enumerate(map(int, input().split())))
    a.sort(key=lambda x: (x[1] - 1) % k, reverse=True)
    result = [a[i][0]+1 for i in range(len(a))]
    print(*result)


for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    