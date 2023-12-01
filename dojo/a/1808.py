import sys
import math
from collections import defaultdict, Counter

def check_lucky(num):
    a = [int(i) for i in str(num)]
    return max(a) - min(a)

def solution():
    m = -1
    l, r = map(int, sys.stdin.readline().split())
    i = l
    while i <= r and m != 9:
        s = list(map(int, list(str(i))))
        u = max(s) - min(s)
        if u > m:
            m = u
            im = i
        i += 1
    print(im)



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()