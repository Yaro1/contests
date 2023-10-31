import sys

def solution():
    ok = True
    n, q = sys.stdin.readline().split()
    n, q = int(n), int(q)
    a = [int(i) for i in sys.stdin.readline().split()]
    q = [int(i) for i in sys.stdin.readline().split()]
    k = 30
    for x in q:
        if x >= k: continue
        for i in range(len(a)):
            if (a[i] % (1 << x) == 0):
                a[i] += (1 << (x - 1))
        k = x
    print(' '.join(str(i) for i in a))

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()


# x % 8 == 0 -> (x + 4) % 16 != 0