def doit(N, k):
    l = list(range(1, N+1))
    l[-k:] = list(reversed(l[-k:]))
    return sum((i+1)*x for i, x in enumerate(l)) - max((i+1)*x for i, x in enumerate(l))

T = int(input())
for t in range(T):
    N = int(input())
    print(max(doit(N, k) for k in range(0, N+1)))
