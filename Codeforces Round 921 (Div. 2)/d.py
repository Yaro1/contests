import sys
 
def solution():
    n, k = map(int, sys.stdin.readline().split())
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    answer = alphabet[:k]
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(answer)
        else:
            result.append(answer[::-1])
    print(''.join(result))
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()