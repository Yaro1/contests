import sys
import math
from collections import defaultdict, Counter

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solution():
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    value_1 = distance(a, c) + distance(a, b) - distance(b, c)
    print(value_1 // 2 + 1)
    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    