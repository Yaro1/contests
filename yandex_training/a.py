import sys

def solution(a):
    l, r = map(int, sys.stdin.readline().split())
    m = min(a[l:r+1])
    for i in range(l, r + 1):
        if m != a[i]:
            print(a[i])
            return
    print("NOT FOUND")


n, m = map(int, sys.stdin.readline().split())
a = [int(i) for i in sys.stdin.readline().split()]
for _ in range(m):
    solution(a)