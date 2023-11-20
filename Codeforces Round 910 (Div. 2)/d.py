for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    u, v, ans = 0, 10 ** 9, 0
    for x, y in zip(a, b):
        u = max(u, min(x, y))
        v = min(v, max(x, y))
        ans += abs(x - y)
    ans += 2 * max(0, u - v)
    print(ans)
