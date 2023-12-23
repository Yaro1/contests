import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(input().split()[0])
    a = []
    for _ in range(n):
        a.append((int(i) for i in input().split()))
    flag_l, flag_r, flag_u, flag_d = True, True, True, True
    for i in range(n):
        x, y = a[i]
        if x < 0:
            flag_l = False
        if x > 0:
            flag_r = False
        if y > 0:
            flag_u = False
        if y < 0:
            flag_d = False
    result = flag_l or flag_r or flag_d or flag_u
    print("YES" if result else "NO")
    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    