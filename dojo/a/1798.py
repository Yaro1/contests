import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in sys.stdin.readline().split()]
    b = [int(i) for i in sys.stdin.readline().split()]
    for i in range(n - 2, -1, -1):
        if ((a[i] > a[-1]) or (b[i] > b[-1])) and ((b[i] > a[-1]) or (a[i] > b[-1])):
            print("NO")
            return
    print("YES")
            



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()