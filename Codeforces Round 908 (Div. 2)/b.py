t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=[1]*n
    out=[]
    for k in set(a):
        if a.count(k)>1:
            out.append(a.index(k))
    if len(out)<2:
        print("-1")
    else:       
        ans[out[0]]=2
        ans[out[1]]=3
        print(*ans)