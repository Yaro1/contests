from heapq import heappush, heappop

def solve():
    n,m=map(int,input().split())
    dct=[[]for i in range(n)]
    for i in range(m):
        a,b,w=map(int,input().split())
        dct[a-1].append([b-1,w])
        dct[b - 1].append([a - 1, w])
    A=list(map(int,input().split()))
    h=[[0,0,A[0]]]
    mp={}
    while h:
        t,p,c=heappop(h)
        if p==n-1:
            print(t)
            return
        if c>A[p]:
            c=A[p]
        if p in mp and mp[p]<=c:
            continue
        else:
            mp[p]=c
        for y,w in dct[p]:
            heappush(h,[t+w*c,y,c])
 
 
 
 
 
for _ in range(int(input())):
    solve()
 