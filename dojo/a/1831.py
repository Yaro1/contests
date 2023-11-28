import sys
import math
from collections import defaultdict

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in sys.stdin.readline().split()]
    value = n + 1
    result = []
    for i in range(len(a)):
        result.append(value - a[i])
    print(*result)



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()