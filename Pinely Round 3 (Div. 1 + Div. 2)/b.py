import sys
import math
from collections import defaultdict, Counter


def solution():
    n = int(input().split()[0])
    a = [int(i) for i in input().split()]
    for i in range(1, 80):
        value = 2 ** i
        if len(set([j % value for j in a])) == 2:
            print(value)
            return
    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    