from sys import stdin
input=lambda :stdin.readline()[:-1]

def solve():
  n,k=map(int,input().split())
  a=list(map(int,input().split()))
  
  ans=max(a)
  for l in range(n):
    ng,ok=10**9,-1
    while abs(ng-ok)>1:
      mid=(ng+ok)//2
      tmp=mid
      cost=0
      flag=False
      for i in range(l,n-1):
        cost+=max(tmp-a[i],0)
        if tmp<=a[i+1]+1 and cost<=k:
          flag=True
        tmp-=1
      if flag:
        ok=mid
      else:
        ng=mid
    ans=max(ans,ok)
    #print(l,ok)
  print(ans)



for _ in range(int(input())):
  solve()