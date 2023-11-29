import sys
import math
from collections import defaultdict, Counter

def solution():
    s = sys.stdin.readline().split()[0]
    if s == "^":
        print(1)
        return
    ans = (s[0] == '_') + (s[-1] == '_')
    for i in range(1, len(s)):
        ans = ans + (s[i] == '_' and s[i-1] == '_')
    print(ans)


for _ in range(int(sys.stdin.readline().split()[0])):
    solution()