import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    print(max(n, m))
    

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solve()
        

        