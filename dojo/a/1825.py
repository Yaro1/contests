import sys
import math
from collections import defaultdict, Counter

def solution():
    s = sys.stdin.readline().split()[0]
    if s[1:] == s[1:][::-1]:
        print(-1)
    else:
        print(len(s)-1)




for _ in range(int(sys.stdin.readline().split()[0])):
    solution()