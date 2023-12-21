import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(input())
    a = [int(i) for i in input().split()]
    s = sum(a)
    cnt_1 = sum(i == 1 for i in a)
    if s >= cnt_1 + n and n > 1:
        print("YES")
    else:
        print("NO")


for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    