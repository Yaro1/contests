import sys
import math
from collections import defaultdict, Counter


def solution():
    n = int(sys.stdin.readline().split()[0])
    s = sorted([i for i in sys.stdin.readline().split()], key=lambda x: len(x))
    print("YES" if s[-1] == s[-2][::-1] else "NO")
    



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()