import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [[-1 for i in range(n)] for _ in range(2)]
    a[0][0], a[-1][-1] = 2*n - 1, 2*n
    for i in range(2, n+1):
        if i % 2 == 0:
            a[0][i - 1] = i
            a[1][i - 2] = i - 1
        else:
            a[0][i - 1] = n + i - 1
            a[1][i - 2] = n + (i - 1) - 1
    print(*a[0])
    print(*a[1])

    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    