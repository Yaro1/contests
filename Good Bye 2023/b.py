import sys
import math
 
def solution():
    a, b = map(int, input().split())
    if a == 1:
        print(b * b)
    else:
        value = math.lcm(a, b)
        if value == b:
            print(b * (b // a))
        else:
            print(value)

 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()

# x % a == 0
# x % b == 0
# 