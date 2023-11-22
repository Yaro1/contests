import sys
import math

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = list(map(int, sys.stdin.readline().split()))
    lb, lc = [], []
    if len(set(a)) == 1:
        print(-1)
        return
    m_value = max(a)
    for i in a:
        if i == m_value:
            lc.append(i)
        else:
            lb.append(i)
    print(len(lb), len(lc))
    print(*lb)
    print(*lc)



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()