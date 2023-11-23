import sys
import math

def solution():
    n, m, k = map(int, sys.stdin.readline().split())
    result = "YES"
    x, y = map(int, sys.stdin.readline().split())
    for _ in range(k):
        xk, yk = map(int, sys.stdin.readline().split())
        if (x+y)% 2 == (xk+yk) % 2:
            result = "NO"
    print(result)




for _ in range(int(sys.stdin.readline().split()[0])):
    solution()