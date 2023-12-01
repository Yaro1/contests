import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in sys.stdin.readline().split()]
    xor = 0
    for i in a:
        xor ^= i
    if xor == 0:
        print(0)
    elif len(a) % 2 == 1:
        print(xor)
    else:
        print(-1)



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()