import sys

def solution():
    n, k = map(int, sys.stdin.readline().split())
    if k > 0:
        answer = [i for i in range(1, k+1)] + [i for i in range(n, k, -1)]
    else:
        answer = [i for i in range(n, 0, -1)]
    print(*answer)

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
        