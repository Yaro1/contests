import sys
import math

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = list(map(int, sys.stdin.readline().split()))
    a_sorted = sorted(a)
    d = {}
    curr_item = 1
    for i in range(len(a_sorted) - 1, -1, -1):
        if a_sorted[i] in d:
            d[a_sorted[i]].append(curr_item)
        else:
            d[a_sorted[i]] = [curr_item]
        curr_item += 1
    answer = []
    for i in a:
        answer.append(d[i].pop())
    print(*answer)

    




for _ in range(int(sys.stdin.readline().split()[0])):
    solution()