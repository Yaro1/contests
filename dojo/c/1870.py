t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    r = -10**18
    l = 10**18
    ans = [0] * k
    for x,i in sorted(zip(a,range(n)),key=lambda x:-x[0]):
        r = max(r,i)
        l = min(l,i)
        ans[x - 1] = 2 * (r - l + 1)
    print(*ans)