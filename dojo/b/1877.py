import sys
import math
from collections import defaultdict, Counter

def solution():
    n, p = map(int, input().split())
    a = [int(j) for j in input().split()]
    b = [int(j) for j in input().split()]
    fin = sorted(list(zip(b, a)))
 
    rem = n-1
    s = p
    for q in fin:
        if (q[0] >= p) or (rem == 0): break
        else:
            take = min(rem, q[1])
            s += take * q[0]
            rem -= take
    s += rem * p
    print(s)


    



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    