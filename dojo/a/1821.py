import sys
import math
from collections import defaultdict, Counter

def is_valid(s):
    s = s.replace("?", "1")
    return int(s) > 0 and s[0] != "0"


def solution():
    s = sys.stdin.readline().split()[0]
    if not is_valid(s):
        print(0)
    else:
        cnt = 1
        if s[0] == "?":
            cnt = 9
        for i in range(1, len(s)):
            if s[i] == "?":
                cnt *= 10
        print(cnt)


for _ in range(int(sys.stdin.readline().split()[0])):
    solution()