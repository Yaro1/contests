import sys
from collections import Counter
 
input = sys.stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    c = Counter((max(2, v) for v in map(int, input().split())))
    print(sum(x * (x - 1) // 2 for x in c.values()))