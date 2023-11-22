import sys
import math

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = list(map(int, sys.stdin.readline().split()))
    flag = False
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            flag = True
    if flag:
        print(0)
        return
    answer = float("inf")
    for i in range(1, len(a)):
        value = a[i] - a[i - 1]
        if value % 2 == 0:
            answer = min(answer, value // 2 + 1)
        else:
            answer = min(answer, math.ceil(value / 2))
    print(answer)

    




for _ in range(int(sys.stdin.readline().split()[0])):
    solution()