import sys

input = sys.stdin.buffer.readline

for _ in range(int(input())):
    n, q = map(int, input().split())

    c = list(map(int, input().split()))

    p = [0] * (n+1)
    for i in range(n):
        p[i] = p[i-1] + c[i]-1 - (c[i] == 1)

    for _ in range(q):
        l, r = map(int, input().split())
        r -= 1
        l -= 1

        if l == r or p[r] - p[l-1] < 0:
            print("NO")
        else:
            print("YES")
