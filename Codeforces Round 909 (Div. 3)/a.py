import sys
    

def solution():
    n = int(sys.stdin.readline().split()[0])
    if n % 3 == 0:
        print("Second")
    else:
        print("First")
    
    

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()


# 0 1 2 3 4 5 6 7 8 9 10
# 996 997 998 999 1000 1001 1002