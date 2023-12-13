import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(input())
    a = [int(j) for j in input().split()]
    b = [int(j) for j in input().split()]
    min_a, sum_a = min(a), sum(a)
    min_b, sum_b = min(b), sum(b)
    print(min(n*min_a + sum_b, n*min_b + sum_a))


for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    