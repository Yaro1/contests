import sys
import math
from collections import defaultdict, Counter

def solution():
    L, R = input().split()
    # n1, n2 = len(s1), len(s2)
    while len(L) < len(R):
        L = '0' + L
    while L and L[0] == R[0]:
        L = L[1:]
        R = R[1:]
    if not L:
        print(0)
    else:
        print(int(R[0]) - int(L[0]) + 9 * (len(L) - 1))
    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    