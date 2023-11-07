import sys

def solution():
    n, m = map(int, sys.stdin.readline().split())
    a = [int(i) for i in sys.stdin.readline().split()]
    b = [int(i) for i in sys.stdin.readline().split()]
    b.sort(reverse=True)
    c, i = [], 0
    for j in a:
        while i < m and b[i] >= j:
            c.append(b[i])
            i += 1
        c.append(j)
    for j in range(i, m):
        c.append(b[j])
    print(*c)


t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()