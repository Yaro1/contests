import sys
import math

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = sum(map(int, sys.stdin.readline().split()))
    if a >= 0:
        print(-a)
    else:
        print(abs(a))
    




for _ in range(int(sys.stdin.readline().split()[0])):
    solution()