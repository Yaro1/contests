import sys

MOD = 1000000007

def cnt_ones(n, bit):
    gsize = (1 << (bit + 1))
    mid = (gsize // 2)
    res = (n // gsize) * mid
    n %= gsize
    if n >= mid:
        res += n - mid + 1
    return res

def solution():
    n = int(sys.stdin.readline().split()[0])
    answer, pow2 = 0, 1
    for bit in range(60):
        cnt  = cnt_ones(n, bit)
        answer += cnt * cnt * pow2
        answer %= MOD
        pow2 *= 2
    print(answer)


t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()