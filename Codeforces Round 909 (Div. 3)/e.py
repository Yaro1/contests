import sys
import math
    

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in sys.stdin.readline().split()]
    m = min(a)
    ind = a.index(m)
    if sorted(a[ind:]) != a[ind:]:
        print(-1)
        return
    print(ind)

    
    
    

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()