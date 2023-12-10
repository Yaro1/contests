import sys

input = sys.stdin.buffer.readline

def d(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

o = [0,0]
for _ in range(int(input())):
    p = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(2)]

    ans = 1e18
    for i in range(2):
        ans = min(ans, max(d(o, a[i]), d(p, a[i])))

    for i in range(2):
        ans = min(ans, max(d(o, a[i]), d(a[0], a[1])/2, d(p, a[i^1])))

    print(ans)
