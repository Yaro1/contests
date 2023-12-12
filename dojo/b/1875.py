import sys
import math
from collections import defaultdict, Counter

def solution():
    n = int(input().split()[0])
    list_sets = []
    full_set = set()
    for _ in range(n):
        a = set([int(i) for i in input().split()[1:]])
        list_sets.append(a)
        full_set = full_set.union(a)
    result = 0
    for number in full_set:
        curr_set = set()
        for s in list_sets:
            if number not in s:
                curr_set = curr_set.union(s)
        result = max(result, len(curr_set))
    print(result)



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()
    