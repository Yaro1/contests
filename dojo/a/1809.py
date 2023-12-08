import sys
import math
from collections import defaultdict, Counter

def solution():
    a = [int(i) for i in sys.stdin.readline().split("\n")[0]]
    if len(set(a)) == 1:
        print(-1)
    elif len(set(a)) == 4 or len(set(a)) == 3:
        print(4)
    elif len(set(a)) == 2:
        if a.count(a[0]) == 1 or a.count(a[0]) == 3:
            print(6)
        else:
            print(4)



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()