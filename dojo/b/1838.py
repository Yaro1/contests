import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(input().split()[0])
    idx = [0 for i in range(n+1)]
    a = [int(i) for i in input().split()]
    for i in range(1, n+1):
        idx[a[i-1]] = i
    if idx[n] < min(idx[1], idx[2]):
        print(idx[n], min(idx[1], idx[2]))
    elif idx[n] > max(idx[1], idx[2]):
        print(idx[n], max(idx[1], idx[2]))
    else:
        print(idx[1], idx[2])
    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    