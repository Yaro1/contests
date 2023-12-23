t = int(input())
for tidx in range(t):
    n = int(input())
    print(*range(3, n+1, 2), 1, *range(n-n%2, 1, -2))