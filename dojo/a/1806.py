import sys
import math
from collections import defaultdict, Counter

def solution():
    a,b,c,d=map(int,input().split())
    x=d-b
    y=a+x-c
    if a+x>=c and b<=d:
        print(x+y)
    else:
        print("-1")



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()