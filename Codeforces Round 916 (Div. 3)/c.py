for x in range(int(input())):
    a,b=map(int,input().split())
    m=list(map(int,input().split()))
    n=list(map(int,input().split()))
    mx=0
    l=0
    crmx=0
    for x in range(min(a,b)):
        l+=m[x]
        crmx=max(crmx,n[x])
        mx=max(mx,l+(crmx)*(b-x-1))
    print(mx)