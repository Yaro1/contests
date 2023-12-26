import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in input().split()]
    a_ = [int(i) for i in input().split()]
    l, r = -1, -1
    for i in range(n):
        if a_[i] != a[i]:
            r = i
            if l == -1:
                l = i
    while l > 0 and a_[l - 1] <= a_[l]:
        l -= 1
    while r < n - 1 and a_[r + 1] >= a_[r]:
        r += 1
    print(l + 1, r + 1)
    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    