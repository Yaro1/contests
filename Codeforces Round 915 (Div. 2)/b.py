import sys
import math
from collections import defaultdict

def solve():
    n = int(sys.stdin.readline().split()[0])
    d = defaultdict(set)
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        d[u].add(v)
        d[v].add(u)
    cnt_lists = 0
    for i in d:
        if len(d[i]) == 1:
            cnt_lists += 1
    print(math.ceil(cnt_lists / 2))
    

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solve()
        

        