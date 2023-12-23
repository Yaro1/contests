import sys
import math
from collections import defaultdict, Counter


def solution():
    n = int(input().split()[0])
    l = [int(i) for i in input().split()]
    r = [int(i) for i in input().split()]
    c = sorted([int(i) for i in input().split()], reverse=True)
    l_r = [(i, 0) for i in l]
    for j in r:
        l_r.append((j, 1))
    l_r.sort(key=lambda x: x[0])
    intervals = []
    stack = []
    for i in range(len(l_r) - 1, -1, -1):
        if l_r[i][1] == 1:
            stack.append(i)
        else:
            intervals.append((l_r[i][0], l_r[stack.pop()][0]))
    intervals.sort(key=lambda x: x[1] - x[0])
    answer = 0
    for i in range(n):
        answer += (intervals[i][1] - intervals[i][0]) * c[i]
    print(answer)
    
    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    