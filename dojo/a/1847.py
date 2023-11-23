import sys
import math

def solution():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    f = []
    s = 0
    for i in range(1, len(a)):
        f.append(abs(a[i] - a[i - 1]))
        s += f[-1]
    f.sort(reverse=True)
    for i in range(k-1):
        s -= f[i]
    print(s)
    



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()