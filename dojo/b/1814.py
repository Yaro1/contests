import sys
import math
from collections import defaultdict, Counter

def solution():
    a, b = map(int, input().split())
    answer = float("inf")
    for k in range(1, 100000):
        answer = min(answer, (a + (k - 1)) // k + (b + (k - 1)) // k + (k - 1))
    print(answer)
    

    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    