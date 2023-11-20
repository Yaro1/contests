import sys
import math

def solution():
    x, k = map(int, sys.stdin.readline().split())
    for i in range(0, 19):
        if sum(int(j) for j in str(x + i)) % k == 0:
            print(x+i)
            return




for _ in range(int(sys.stdin.readline().split()[0])):
    solution()