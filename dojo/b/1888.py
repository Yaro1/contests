import sys
import math
from collections import defaultdict, Counter

def solution():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
 
    candidates = [min((k - v % k) % k for v in a)]
    if k == 4:
        mod2 = sum(v % 2 == 0 for v in a)
        candidates.append(max(0, 2 - mod2))
    
    print(min(candidates))

    



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()