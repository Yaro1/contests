import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    c = list(map(int, input().split()))
    S = [0] * (n + 1)
    for i in range(n):
        S[i + 1] = S[i] + (-1 if c[i] == 1 else c[i] - 1)
    for _ in range(q):
        l, r = map(int, input().split())
        print("YES" if l != r and S[r] - S[l - 1] >= 0 else "NO")
