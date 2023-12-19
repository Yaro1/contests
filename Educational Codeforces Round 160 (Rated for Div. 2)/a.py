import sys

def dividing(s):
    b = 1
    while b < len(s) and s[b] == '0':
        b += 1
    if b == len(s):
        return float("inf"), 0
    return int(s[:b]), int(s[b:])

def solution():
    s = input()
    a, b = dividing(s)
    if a >= b:
        print(-1)
    else:
        print(a, b)
    

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
        