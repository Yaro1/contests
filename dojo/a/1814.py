import sys
import math
from collections import defaultdict, Counter

def solution():
    n, k = map(int, sys.stdin.readline().split())
    if (n - k) % 2 == 0:
        print("YES")
    elif n % 2 == 0:
        print("YES")
    else:
        print("NO")



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()