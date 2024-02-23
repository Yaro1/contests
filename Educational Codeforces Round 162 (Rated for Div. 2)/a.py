import sys

def solution():
    n = int(input())
    a = [int(i) for i in input().split()]
    answer = 0
    zeros = []
    first, last = 0, 0
    for i in range(len(a)):
        if a[i] == 1:
            first = i
            break
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 1:
            last = i
            break
    for i in range(first, last + 1):
        if a[i] == 0:
            zeros.append(i)
    ones = []
    for i in range(first, last + 1):
        if a[i] == 1:
            ones.append(i)
    while zeros:
        ones[-1] = zeros.pop()
        ones.sort()
        answer += 1
    print(answer)


        
    

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
        