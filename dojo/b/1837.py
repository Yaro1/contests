import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(sys.stdin.readline().split()[0])
    s = input()
    d = {
        ">": 0,
        "<": 0,
    }
    greater, less = 0, 0
    curr_item = s[0]
    if curr_item == ">":
        greater += 1
    else:
        less += 1
    for i in range(1, len(s)):
        if s[i] == ">" and curr_item == s[i]:
            greater += 1
        elif s[i] == ">" and curr_item != s[i]:
            d[curr_item] = max(d[curr_item], less)
            less = 0
            greater = 1
            curr_item = s[i]
        elif s[i] == "<" and curr_item == s[i]:
            less += 1
        elif s[i] == "<" and curr_item != s[i]:
            d[curr_item] = max(d[curr_item], greater)
            greater = 0
            less = 1
            curr_item = s[i]
    d[">"] = max(d[">"], greater)
    d["<"] = max(d["<"], less)
    if d[">"] > d["<"]:
        print(d[">"] + 1)
    else:
       print(d["<"] + 1)
    

for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    