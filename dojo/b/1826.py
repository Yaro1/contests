from math import gcd
for t in range(int(input())):
    n = int(input())
    a = [int(s) for s in input().split()]
    x = 0
    for i in range(n//2):
        x = gcd(x,abs(a[i]-a[n-i-1]))
    print(x)