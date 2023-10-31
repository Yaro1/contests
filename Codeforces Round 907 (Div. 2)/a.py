import sys

def is_power(item):
    s = 1
    while s < item:
        s *= 2
    if s == item:
        return True
    else:
        return False

def solution():
    ok = True
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in sys.stdin.readline().split()]
    for i in range(n-1):
        if a[i] > a[i + 1] and not is_power(i + 1):
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()