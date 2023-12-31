import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) if int(i) != 1 else 2 for i in input().split()]
    for i in range(1, len(a)):
        if a[i] % a[i - 1] == 0:
            a[i] += 1
    print(*a)

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    