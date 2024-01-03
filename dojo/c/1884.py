for t in range(int(input())):
    n,m=map(int,input().split())
    a,b,c,d,e=[],0,0,0,0
    for i in range(n):
        j,k=map(int,input().split())
        a.append((j-1,k))
        a.append((k,j-1))
    for i,j in sorted(a):
        if i<j:b+=1
        else:b-=1
        if i==0:c+=1
        if j==0:c-=1
        if j==m:d+=1
        if i==m:d-=1
        e=max(b-min(c,d),e)
    print(e)