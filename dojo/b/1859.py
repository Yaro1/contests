t = int(input())
for q in range(t):
    n = int(input())
    mn = 10000000000
    b = []
    for j in range(n):
        m = int(input())
        a = sorted([int(i) for i in input().split()])
        mn = min(mn, a[0])
        b.append(a[1])
    print(sum(b)-min(b)+mn)
