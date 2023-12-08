import sys
import math
from collections import defaultdict, Counter


def solution():
    n = int(sys.stdin.readline().split()[0])
    s = input()
    string = "FBFFBFFB"
    string_checking = (math.ceil(len(s) / len(string)) + 2) * string
    print("YES" if s in string_checking else "NO")
    



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()