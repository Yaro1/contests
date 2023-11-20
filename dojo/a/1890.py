import sys

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = list(map(int, sys.stdin.readline().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    if len(d) > 2:
        print("No")
    else:
        if len(d) == 1:
            print("Yes")
            return
        keys = list(d.keys())
        if abs(d[keys[0]] - d[keys[1]]) <= 1:
            print("Yes")
            return
        print("No")



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()