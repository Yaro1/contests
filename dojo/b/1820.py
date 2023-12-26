import sys
import math
from collections import defaultdict, Counter

def solution():
    s=input()
    c=0
    m=0
    for i in range(2*len(s)-1):
        if s[i%len(s)]=="1":
            c+=1
        else:
            c=0
        m=max(m,c)
    print(((m+1)*(m+1))//4)

    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    