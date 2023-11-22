import sys
import math

def solution():
    n = int(sys.stdin.readline().split()[0])
    p = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    for i in range(len(p)):
        if i+1 == p[i]:
            cnt += 1
    if cnt % 2 == 0:
        print(cnt // 2)
    else:
        print(cnt // 2 + 1)



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()