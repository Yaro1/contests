import sys
from bisect import bisect_left


def sort_find_append_min_diff(l):
    l.sort()
    m = float("inf")
    for i in range(1, len(l)):
        m = min(abs(l[i] - l[i - 1]), m)
    l.append(m)
    return l

def solve():
    n, k = map(int, sys.stdin.readline().split())
    h = [int(i) for i in sys.stdin.readline().split()]
    if k >= 3:
        print(0)
        return
    h.sort()
    m = h[0]
    for i in range(1, len(h)):
        m = min(m, h[i] - h[i - 1])
    if k == 1:
        print(m)
    else:
        for i in range(len(h)):
            for j in range(i):
                v = h[i] - h[j]
                p = bisect_left(h, v)
                if p < n:
                    m = min(m, h[p] - v)
                if p > 0:
                    m = min(m, v - h[p - 1])
        print(m)


t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solve()


# 20 5 1 4 2
# 1 2 4 5 20
# 1 3 7 12 32