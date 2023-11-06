t = int(input())
for _ in range(t):
    n = int(input())
    ax = [*map(int, input().split())]
    ay = [*map(int, input().split())]
    a = []
    for x, y in zip(ax, ay):
        a.append((x, y))
    m = int(input())
    bx = [*map(int, input().split())]
    by = [*map(int, input().split())]
    b = []
    for x, y in zip(bx, by):
        b.append((x, y))
    a.sort(key=lambda z: z[1], reverse=True)
    b.sort(key=lambda z: z[0], reverse=True)
    aa, bd = [0] * (n + 1), [0] * (m + 1)
    for i in range(n):
        aa[i + 1] = max(aa[i], a[i][0])
    for i in range(m):
        bd[i + 1] = max(bd[i], b[i][1])
    k = s = t = 0
    for i in range(n):
        while k < m and a[i][1] < b[k][0]:
            k += 1
        if k == 0:
            s = i + 1
        else:
            if aa[s] > bd[k]:
                s = i + 1
            elif aa[i + 1] > bd[k]:
                t = i + 1
    print(s, max(0, t - s), n - max(s, t))