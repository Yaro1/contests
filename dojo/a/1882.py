import sys
import math

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = list(map(int, sys.stdin.readline().split()))
    b = 0
    for i in range(len(a)):
        b = b+1 if b+1 != a[i] else b + 2
    print(b)


    




for _ in range(int(sys.stdin.readline().split()[0])):
    solution()