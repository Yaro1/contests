import sys

import math

def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n//i])
    divs.extend([n])
    return set(divs)
 
def solution():
    x, n = map(int, sys.stdin.readline().split())
    answer = -1
    for i in divisors(x):
        if x // i >= n:
            answer = max(answer, i)
    print(answer)

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()