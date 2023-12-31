t=int(input())
for _ in range(t):
  n,k=map(int,input().split())
  f=False
  s=False
  for _ in range(n):
    a,b=map(int,input().split())
    if b==k:s=True
    if a==k:f=True
  print('YES' if (f and s) else 'NO')
