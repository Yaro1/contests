import sys
from collections import Counter
 
def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in sys.stdin.readline().split()]
    if 0 in a:
        print(0)
        return
    flag_negative = sum([True if i < 0 else False for i in a])
    if flag_negative % 2 == 1:
        print(0)
    else:
        print(1)
        print(1, 0)
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
        