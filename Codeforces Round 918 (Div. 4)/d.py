import sys
 
V = set(['a', 'e'])
C = set(['b', 'c', 'd'])


def solution():
    n = int(sys.stdin.readline().split()[0])
    s = input()
    res = []
    type_slog = -1
    i = n - 1
    while i > 0:
        if s[i] in C:
            res.append(s[i-2:i+1])
            i -= 3
        else:
            res.append(s[i-1:i+1])
            i -= 2
    print('.'.join(res[::-1]))

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()