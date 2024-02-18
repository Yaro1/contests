import sys
import math
 
def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in sys.stdin.readline().split()]
    for i in range(1, len(a)):
        if a[i] <= a[i - 1]:
            if a[i] == a[i - 1]:
                a[i] += a[i]
            else:
                value = a[i - 1] // a[i]
                a[i] += (value * a[i])
    print(a[-1])
            




t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()

# 3 2 4 5 9 18
# 3 4 8 10 18 36
# 

