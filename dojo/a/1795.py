import sys
import math
from collections import defaultdict, Counter


def solution():
    n, m = map(int, sys.stdin.readline().split())
    s, t = input(), input()[::-1]
    s = s + t
    cnt = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt += 1
    print("YES" if cnt <= 1 else "NO")
    
    



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()