import sys
import math
from collections import defaultdict, Counter

def solution():
    n, k = map(int, sys.stdin.readline().split())
    x = -1

    for i in range(0, n + 1):
        if i * (i - 1) / 2 + (n - i) * (n - i - 1) / 2 == k:
            x = i

    if x == -1:
        print("NO")
    else:
        print("YES")
        for i in range(0, n):
            if i < x:
                print("1 ", end = '')
            else:
                print("-1 ", end = '')
        print("")



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()