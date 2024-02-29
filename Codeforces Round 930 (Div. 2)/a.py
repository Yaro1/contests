import sys
 
def solution():
    n = int(sys.stdin.readline().split()[0])
    ind = 1
    while ind <= n:
        ind *= 2
    print(ind // 2)
    
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
