import sys
from collections import Counter

def solution():
    s = input()
    d = {
        '0': 0,
        '1': 0
    }
    for i in s:
        d[i] += 1
    result_str = []
    for i in range(len(s)):
        if s[i] == '0' and d['1'] > 0:
            result_str.append('1')
            d['1'] -= 1
        elif s[i] == '0' and d['1'] == 0:
            break
        elif s[i] == '1' and d['0'] > 0:
            result_str.append('0')
            d['0'] -= 1
        elif s[i] == '1' and d['0'] == 0:
            break
    print(len(s) - len(result_str))

    

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
        