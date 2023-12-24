import sys
from collections import Counter
from functools import lru_cache
 
def solution():
    n = int(sys.stdin.readline().split()[0])
    s = sys.stdin.readline().split()[0]
    mn = set()
    cnt = 0
    for i in range(len(s)):
        mn.add(s[i])
        cnt += len(mn)
    print(cnt)

 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
        