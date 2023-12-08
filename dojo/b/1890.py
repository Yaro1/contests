import sys
import math
from collections import defaultdict, Counter

def is_good(a):
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            return False
    return True


def solution():
    n, m = map(int, sys.stdin.readline().split())
    s, t = input(), input()
    if is_good(s):
        print("YES")
    elif is_good(t) and t[0] == "1" and t[-1] == "1" and "11" not in s:
        print("YES")
    elif is_good(t) and t[0] == "0" and t[-1] == "0" and "00" not in s:
        print("YES")
    else:
        print("NO")

    



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()