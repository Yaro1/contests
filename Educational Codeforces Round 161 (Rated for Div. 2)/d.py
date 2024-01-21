import sys,math,bisect
from collections import deque
input=sys.stdin.readline
mod=998244353
def f(a):
    n=len(a)
    pre=[0]*(n) 
    dp=[0]*(n) 
    dp2=[0]*(n) 
    dp[0]=1
    pre[0]=1
    dp2[0]=1
    stack=[0]
    for i in range(1,n):
        while stack:
            if a[stack[-1]]>a[i]:
                stack.pop()
            else:
                break
        if stack:
            t=stack[-1]
            dp[i]=(pre[i-1]-pre[t]+dp2[t])%mod
            dp2[i]=(dp[i]+dp2[t])%mod 
        else:
            dp[i]=(pre[i-1]+1)%mod 
            dp2[i]=dp[i]
        stack.append(i)
        pre[i]=(pre[i-1]+dp[i])%mod
    return dp
for _ in range(int(input())):
    n=int(input())
    #n,q=map(int,input().split())
    a=list(map(int,input().split()))
    t=min(a)
    for i in range(n):
        if a[i]==t:
            x=i 
            break
    ansleft=f(a)[x]
    a.reverse()
    ansright=f(a)[n-x-1]
    print((ansleft*ansright)%mod)
        
        