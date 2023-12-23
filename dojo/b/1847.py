import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(input().split()[0])
    a = [int(i) for i in input().split()]
    curr = a[0]
    parts = 1
    for i in range(len(a)):
        curr &= a[i]
        if curr == 0:
            if i == len(a) - 1:
                break
            parts += 1
            curr = a[i + 1]
    if curr != 0:
        parts -= 1
    parts = max(parts, 1)
    print(parts)
    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    