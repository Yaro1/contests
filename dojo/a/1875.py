import sys
import math

def solution():
    a, b, n = map(int, sys.stdin.readline().split())
    x = map(int, sys.stdin.readline().split())
    time_to_dead = b
    for i in x:
        time_to_dead += min(i, a - 1)
    print(time_to_dead)


    




for _ in range(int(sys.stdin.readline().split()[0])):
    solution()