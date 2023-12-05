def sol(arrs):
    l, h = 0, 10**9
    while l < h:
        minp, maxp = 0, 0
        k = (l + h) // 2
        ok = True
        for arr in arrs:
            minp = max(minp, arr[0])
            maxp = min(maxp + k, arr[1])
            if minp > maxp:
                ok = False
                break
            minp = max(minp - k, 0)
        if ok:
            h = k
        else:
            l = k + 1
    return l
 
 
t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    print(sol(a))