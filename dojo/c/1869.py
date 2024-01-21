import sys
import math
from collections import defaultdict, Counter

def solution():
    n,m = [int(i) for i in input().split()]
    if m == 1:
        for i in range(n+1):
	        print(0)
    else:
	    print(min(n+1, m))
	    for i in range(n):
	    	d = i % (m-1)
	    	print(' '.join([str((i+d)%m) for i in range(m)]))
    
# 0 1 2
# 2 0 1
# 1 2 0
    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    