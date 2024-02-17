import sys
 
def solution():
    n = int(sys.stdin.readline().split()[0])
    a = sorted([int(i) for i in sys.stdin.readline().split()])
    answer = 0
    for i in range(0, 2*n, 2):
        answer += a[i]
    print(answer)
    
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
