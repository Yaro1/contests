import sys
import math

def solution():
    a, b = sorted(map(int, sys.stdin.readline().split()))
    if a == 1 and b == 2:
        print(3)
    elif a == 1:
        print(2)
    else:
        print(1)




for _ in range(int(sys.stdin.readline().split()[0])):
    solution()