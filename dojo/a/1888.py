import sys

def solution():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().split()[0]
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    d_even = sum(1 for i in d if d[i] % 2 == 1)
    if k >= d_even:
        print("YES")
    else:
        if d_even - k > 1:
            print("NO")
        else:
            print("YES")




for _ in range(int(sys.stdin.readline().split()[0])):
    solution()