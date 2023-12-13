import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(input())
    s = input()
    c = 0
    ans = ['0'] * (n + 1)
    for i in range(n // 2):
        c += int(s[i] != s[n - i - 1])
    if n & 1:
        for i in range(c, n - c + 1):
            ans[i] = '1'
    else:
        for i in range(c, n - c + 1, 2):
            ans[i] = '1'
    print(''.join(ans))


for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    