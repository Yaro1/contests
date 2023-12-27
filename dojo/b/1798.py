import sys
import math
from collections import defaultdict, Counter

def solution():
    m = int(sys.stdin.readline().split()[0])
    days = []
    for i in range(m):
        n = int(sys.stdin.readline().split()[0])
        days.append([int(i) for i in sys.stdin.readline().split()])
    d = {}
    for i in range(len(days)):
        for j in range(len(days[i])):
            d[days[i][j]] = i
    answer = [-1 for i in range(len(days))]
    for i in d:
        answer[d[i]] = i
    if -1 not in answer:
        print(*answer)
    else:
        print(-1)
    
    

    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    