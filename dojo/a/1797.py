import sys
import math
from collections import defaultdict, Counter

def check_point(point, n, m):
    cnt = 0
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for i in d:
        if (1 <= point[0] + i[0] <= n) and (1 <= point[1] + i[1] <= m):
            cnt += 1
    return cnt

def solution():
    n, m = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(min(check_point((x1, y1), n, m), check_point((x2, y2), n, m)))



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()