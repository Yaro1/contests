import sys
from collections import Counter

def solve():
    n = int(sys.stdin.readline().split()[0])
    s = sys.stdin.readline().split()[0]
    d = Counter(s)
    items = sorted([(i, j) for i, j in d.items()], key=lambda x: x[1])
    if n % 2 == 0:
        if items[-1][1] > (n - items[-1][1]):
            print(items[-1][1] - (n - items[-1][1]))
        else:
            print(0)
    else:
        if items[-1][1] > (n - items[-1][1]):
            print(items[-1][1] - (n - items[-1][1]))
        else:
            print(1)

        


t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solve()
        

# -3 -4 2 -5 1 10 17 23

# [-3] [-4] [2] [-5] [1] [10] [17] [23]