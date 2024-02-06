import sys
 
def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in sys.stdin.readline().split()]
    q = int(sys.stdin.readline().split()[0])
    queries = []
    for i in range(q):
        l, r = map(int, sys.stdin.readline().split())
        queries.append((l, r))
    a_fixed = [[i, len(a)] for i in range(len(a))]
    l, r = 0, 0
    while l < len(a):
        while r < len(a) and a[r] == a[l]:
            r += 1
        while l < r:
            a_fixed[l][1] = r
            l += 1
    for query in queries:
        if a_fixed[query[0] - 1][1] != len(a) and a_fixed[query[0] - 1][1] + 1 <= query[1]:
            print(query[0], a_fixed[query[0] - 1][1] + 1)
        else:
            print(-1, -1)

 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()