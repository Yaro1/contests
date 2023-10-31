import sys
input = lambda: sys.stdin.readline()[:-1]
q = int(input())
 
mod = 10**9 + 7
def logsum(l, r, k):
    total = 0
    cur = 1
    val = 0
    while cur <= r:
        curl = max(cur, l)
        curr = min(cur*k, r)
        if curl < curr:
            total += val * (curr - curl)
            total %= mod
        cur *= k
        val += 1
    return total
 
for _ in range(q):
    l, r = [int(i) for i in input().split()]
    total = 0
    for i in range(2, 62):
        curl = max(2**i, l)
        curr = min(2**(i+1), r+1)
        if curl >= curr: continue
        total += logsum(curl, curr, i)
        total %= mod
    print(total)
