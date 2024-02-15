import sys
 
def solution():
    n = int(sys.stdin.readline().split()[0])
    a = sorted([int(i) for i in sys.stdin.readline().split()])
    res = 0
    for i in range(1, len(a)):
        res += a[i] - a[i - 1]
    print(res)
    
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
