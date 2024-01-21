i=input
for _ in range(int(i())):
    n,m,k=list(map(int,i().split()))
    a=min(m,n-1)+m//n
    print([1,a,m-a,0][min(k,4)-1])