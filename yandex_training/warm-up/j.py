import sys

def solution():
    n, a, b = map(int, sys.stdin.readline().split())
    a, b = min(a, b), max(a, b)
    value = n % a
    groups = n // a
    print("YES") if value <= groups * (b - a) else print("NO")


t = int(sys.stdin.readline().split()[0])
# t = 1
for _ in range(t):
    solution()