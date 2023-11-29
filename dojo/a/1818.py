import sys
import math
from collections import defaultdict, Counter

def solution():
    n, k = map(int, sys.stdin.readline().split())
    ans = 1
    x = input()
    for i in range(n-1):
        if input() == x:
            ans += 1
    print(ans)



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()