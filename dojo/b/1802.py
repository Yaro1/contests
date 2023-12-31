for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c1=c2=res=0
    for i in range(len(l)):
        if l[i]==1:c1+=1
        else:c2+=c1;c1=0
        res=max(res,c2//2+(c2>0)+c1)
    print(res)