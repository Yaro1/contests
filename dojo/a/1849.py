import sys
import math

def solution():
    b, c, h = map(int, sys.stdin.readline().split())
    b, ch = b - 2, c + h
    if b >= ch:
        print(2 * ch + 1)
    else:
        print(3 + 2 * b)




for _ in range(int(sys.stdin.readline().split()[0])):
    solution()