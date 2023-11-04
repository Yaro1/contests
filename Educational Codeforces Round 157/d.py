n = int(input())
a = list(map(int, input().split()))
b = [0] * n
x = sum(range(n))
for i in range(1, n):
    b[i] = b[i - 1] ^ a[i - 1]
b[0] = 0
for i in range(31):
    cnt = sum((x >> i) & 1 for x in b)
    cnt2 = sum((j>>i) & 1 for j in range(n))
    if cnt != cnt2:
        b[0] |= (1 << i)
for i in range(1, n):
    b[i] ^= b[0]
 
print(*b)