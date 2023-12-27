import sys
import math
from collections import defaultdict, Counter

def solution():
    n, m = map(int, sys.stdin.readline().split())
    answer = 0
    d = defaultdict(list)
    for i in range(n):
        a = [int(i) for i in sys.stdin.readline().split()]
        for j in range(len(a)):
            d[j].append(a[j])
    for i in d:
        d[i].sort()
        p = [d[i][j] for j in range(len(d[i]))]
        for j in range(1, len(p)):
            p[j] += p[j - 1]
        for j in range(len(p)):
            answer += d[i][j] * (j + 1) - p[j]
    print(answer)
    
    

    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    