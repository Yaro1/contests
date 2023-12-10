import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(sys.stdin.readline().split()[0])
    s = sys.stdin.readline().split()[0]
    # print(s)
    zeros = [i for i in range(n) if s[i]=='0']
    ansl = [0]
    for i in range(n-1, -1, -1):
        if not zeros:
            ansl.append(-1)
        else:
            ansl.append(ansl[-1]+i-zeros.pop())
    print(*ansl[1:])


    



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()