import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(sys.stdin.readline().split()[0])
    s = input()
    m_value, ind = s[0], 0
    for i in range(1, len(s)):
        if s[i] <= m_value:
            m_value = s[i]
            ind = i
    if ind != 0:
        print(''.join([s[ind], s[:ind] + s[ind+1:]]))
    else:
        print(s)
    

    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    