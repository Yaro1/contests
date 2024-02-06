import sys
 
def solution():
    n, k, m = map(int, input().split())
    s = input()
    al = 'abcdefghijklmnopqrstuvwxyz'
    sal = al[:k]
    d = {}
    cnt = 0
    l = []
    for i in s:
        d[i] = None
        if len(d) == k:
            l.append(i)
            d = {}
    if len(l) < n:
        print('NO')
        c = "."
        for i in sal:
            if i not in d:
                c = i
                break
        print(''.join(l + [c for i in range(n - len(l))]))
    else:
        print('YES')
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()