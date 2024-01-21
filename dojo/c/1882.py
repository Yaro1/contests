for _ in range(int(input())):
    n=int(input())
    lis=list(map(int,input().split()))
    ans=0
    if n>1:
        ans+=max(0,lis[0]+max(0,lis[1]))
    else:
        ans+=max(0,lis[0])
    for i in range(2,n):
        ans+=max(0,lis[i])
    print(ans)