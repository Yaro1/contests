from itertools import groupby

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    groups = [0] * (2 * n + 1)
    ans = 0
    for k, v in groupby(a):
        groups[k] = max(groups[k], len(list(v)))
        ans = max(ans, groups[k])
    for k, v in groupby(b):
        ans = max(ans, len(list(v)) + groups[k])
    print(ans)