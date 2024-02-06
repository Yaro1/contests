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
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in sys.stdin.readline().split()]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = [-1 for i in range(n)]
    for i in alphabet:
        current_num = 0
        for j in range(len(a)):
            if a[j] == current_num:
                result[j] = i
                a[j] = -1
                current_num += 1
    print(''.join(result))
            




t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()