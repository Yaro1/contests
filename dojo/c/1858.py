t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    for i in range(1,n+1,2):
        j=i
        while(j<=n):
            a.append(j)
            j*=2
    print(*a)