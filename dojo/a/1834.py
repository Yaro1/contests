import sys
import math
from collections import defaultdict

# cnt_-1 <= cnt_1
# cnt_-1 % 2 == 0 

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in sys.stdin.readline().split()]
    cnt_minus, cnt_plus = 0, 0
    for i in a:
        if i == -1:
            cnt_minus += 1
        else:
            cnt_plus += 1
    if cnt_minus <= cnt_plus and cnt_minus % 2 == 0:
        print(0)
    elif cnt_minus > cnt_plus:
        result = math.ceil((cnt_minus - cnt_plus) / 2)
        if (cnt_minus - result) % 2 == 1:
            print(result + 1)
        else:
            print(result)
    elif cnt_minus <= cnt_plus and cnt_minus % 2 == 1:
        print(1)



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()