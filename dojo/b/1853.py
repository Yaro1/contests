import sys
import math
from collections import defaultdict, Counter

def solution():
    n,k=map(int,input().split())
    ans=0
    for i in range(n//2+1):
        a,b=i,n-i
        t=k-2
        while t and b>=a and a>=0:
            piche=b-a
            b=a
            a=piche
            t-=1
        if t==0:
            ans+=1
    print(ans)


for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    