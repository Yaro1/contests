import sys
import math

def solution():
    n, k, x = map(int, sys.stdin.readline().split())
    if min(n, x+1) < k:
        print(-1)
        return
    print( k * (k-1) // 2 + (n-k)*(x-1 if k == x else x))




for _ in range(int(sys.stdin.readline().split()[0])):
    solution()