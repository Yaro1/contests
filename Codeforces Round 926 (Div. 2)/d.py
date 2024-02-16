mod = 998244353
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    g = [[] for k in range(n)]
    d = [0] * n
    for i in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        d[u] += 1
        d[v] += 1
    q = [i for i in range(n) if d[i] == 1]
    dp = [1] * n
    ans = 1
    for v in q:
        d[v] -= 1
        for u in g[v]:
            if d[u] == 0:
                ans = (ans + dp[u]) % mod
                continue
            d[u] -= 1
            if d[u] == 1:
                q.append(u)
            dp[u] = dp[u] * (dp[v] + 1) % mod
    ans = (ans + dp[q[-1]]) % mod
    print(ans)
