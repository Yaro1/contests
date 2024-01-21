import sys
import math
from collections import defaultdict, Counter

def solution():
    n=int(input())
    s=list(map(int,input().split()))
    now=0
    for i in s:
        if i!=now:
            break
        now+=1
    while True:
        print(now,flush=True)
        y=int(input())
        now=y
        if y<0:
            break
    
    

    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    