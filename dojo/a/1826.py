import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(sys.stdin.readline().split()[0])
    l = [int(i) for i in sys.stdin.readline().split()]
    for i in range(0, n+1):
        liers = 0
        for j in range(n):
            if l[j] > i:
                liers += 1
        if liers == i:
            print(liers)
            return
    print(-1)



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()