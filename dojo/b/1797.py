import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n,k=map(int,input().split())
    x=[]
    for _ in range(n):
        x.append(tuple(map(int,input().split())))
    value=0
    for i in range(n):
        for j in range(n):
            value+=x[i][j]!=x[n-1-i][n-1-j]
    value//=2
    print("YES" if k>=value and (n&1 or not (k-value)&1) else "NO")
