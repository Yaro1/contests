import sys
import math
from collections import defaultdict, Counter

def solution():
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = 0
    for i in b:
        c |= i
    x, y = 0, 0
    for i in a:
        x ^= i | c
        y ^= i
    print(min(x, y), max(x, y))


for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    