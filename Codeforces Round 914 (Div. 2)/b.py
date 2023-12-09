import sys
from bisect import bisect_right

def solve():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in sys.stdin.readline().split()]
    b = sorted(a)
    prefix_b = [[b[0], b[0]]]
    d_prefix_b = {b[0]: b[0]}
    i = 1
    while i < len(b):
        if b[i] != b[i - 1]:
            prefix_b.append([b[i], prefix_b[-1][1] + b[i]])
            d_prefix_b[b[i]] = prefix_b[-1][1]
        else:
            prefix_b[-1][1] += b[i]
            d_prefix_b[b[i]] += b[i]
        i += 1
    
    for i in range(len(prefix_b) - 2, -1, -1):
        if prefix_b[i][1] >= prefix_b[i + 1][0]:
            prefix_b[i][1] = prefix_b[i+1][1]
            d_prefix_b[prefix_b[i][0]] = prefix_b[i][1]
    # print(d_prefix_b)
    d = {}
    for i in d_prefix_b:
        d[i] = bisect_right(b,d_prefix_b[i])

    result = []
    for i in range(len(a)):
        result.append(d[a[i]] - 1 if d[a[i]] != 0 else 0)
    print(*result)


t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solve()


# 20 5 1 4 2
# 1 2 4 5 20
# 1 3 7 12 32