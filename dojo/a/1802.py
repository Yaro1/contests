import sys
import math
from collections import defaultdict, Counter

def solution():
    sz = int(input())
    temp = list(map(int, input().split()))
    cnt = 0
    for i in temp:
        if i < 0:
            cnt += 1
    pos = sz - cnt
    print(*([i+1 for i in range(pos)] + [pos - i - 1 for i in range(cnt)]))
    x = [1, 0] * cnt + [i+1 for i in range(pos-cnt)]
    print(*x)



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()