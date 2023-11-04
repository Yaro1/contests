import sys
 
def solution():
    x, y, k = map(int, sys.stdin.readline().split())
    if x == y:
        print(x)
    elif x > y:
        print(x)
    elif x < y:
        value = min(x+k, y)
        print(2*y - value)
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()