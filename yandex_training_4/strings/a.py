import sys


def solution():
    l, a, b = map(int, sys.stdin.readline().split())
    flag = True
    for i in range(l):
        if s[a+i] != s[b+i]:
            flag = False
            break
    print("yes" if flag else "no")


s = sys.stdin.readline().split()[0]
q = int(sys.stdin.readline().split()[0])
for _ in range(q):
    solution()