import sys

input = sys.stdin.buffer.readline

MOD = 998244353

def choose(n, k):
    res = 1

    for i in range(k):
        res *= (n-i)
        res %= MOD
    for i in range(1, k+1):
        res *= pow(i, -1, MOD)
        res %= MOD

    return res

for _ in range(int(input())):
    n, C = map(int, input().split())

    ch = [() for _ in range(n+1)]
    vals = [0] * (n+1)

    for i in range(1, n+1):
        l, r, val = map(int, input().split())
        vals[i] = val
        ch[i] = (l, r)

    a = [1]

    s = [1]
    vis = [0] * (n+1)
    while s:
        c = s[-1]

        if c == -1:
            s.pop()
            continue

        if not vis[c]:
            vis[c] = 1
            s.append(ch[c][0])
        else:
            a.append(vals[c])
            s.pop()
            s.append(ch[c][1])
    a.append(C)

    ans = 1

    i = 0
    while i < len(a):
        j = i+1
        while j < len(a) and a[j] == -1:
            j += 1

        if j == len(a):
            break
        else:
            num_neg1 = j-i-1
            ans *= choose(a[j]-a[i] + num_neg1, num_neg1)
            ans %= MOD

            i = j

    print(ans)
