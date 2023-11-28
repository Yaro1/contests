import sys
import math
from collections import defaultdict

def solution():
    n = int(sys.stdin.readline().split()[0])
    l = [int(i) for i in sys.stdin.readline().split()]
    d = defaultdict(int)
    for i in l:
        d[i] += 1
    m_value = max(d.items(), key=lambda x: x[0])[0]
    for i in range(1, m_value+1):
        if (i not in d) or (i - 1 not in d) or (d[i] > d[i - 1]):
            print("NO")
            return
    print("YES")



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()