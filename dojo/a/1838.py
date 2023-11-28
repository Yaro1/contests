import sys
import math
from collections import defaultdict

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = sorted([int(i) for i in sys.stdin.readline().split()])
    if a[0] < 0:
        print(a[0])
    else:
        print(a[-1])
    



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()