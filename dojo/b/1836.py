import sys
import math
from collections import defaultdict, Counter

def solution():
    n,k,g=map(int,input().split())
    if k==0:
        print(0)
    else:
        half=(g-1)//2
        print(min((n*half)//g*g,k*g))
    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    