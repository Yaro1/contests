import sys
from collections import Counter
 
def solution():
    n = int(sys.stdin.readline().split()[0])
    s = 'abcdefghijklmnopqrstuvwxyz'
    j = Counter(input())
    cnt = 0
    for num, i in enumerate(s):
        if i.upper() in j and num + 1 <= j[i.upper()]:
            cnt += 1
    print(cnt)
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
        