import sys
import math

def solution():
    a, b, c = map(int, sys.stdin.readline().split())
    ann = a + c // 2 + (1 if c % 2 == 1 else 0  )
    kate = b + c // 2
    if ann > kate:
        print("First")
    else:
        print("Second")



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()