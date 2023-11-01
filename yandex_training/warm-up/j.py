import sys

def solution():
    n, a, b = map(int, sys.stdin.readline().split())
    for i in range(a, b + 1):
        if (n % i == 0) or (a <= (n % i) <= b):
            print(i, n % i)
            print("YES")
            return
    print("NO")

# 2*5 + 3*17 + 1*29


t = int(sys.stdin.readline().split()[0])
# t = 1
for _ in range(t):
    solution()