import sys
import math

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = []
    for _ in range(n):
        s, e = map(int, sys.stdin.readline().split())
        a.append((s, e))
    weight, winner, winner_cnt = a[0][0], 0, 0
    for i in range(len(a)):
        if a[i][0] >= weight:
            if winner < a[i][1]:
                winner = a[i][1]
                winner_cnt = 1
            elif winner == a[i][1]:
                winner_cnt += 1
    if winner_cnt > 1 or a[0][1] != winner:
        print(-1)
    else:
        print(a[0][0])




for _ in range(int(sys.stdin.readline().split()[0])):
    solution()