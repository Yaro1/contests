mod=1_000_000_007
 
 
 
t=int(input())
for testid in range(t):
	n,x,k=map(int,input().split())
	ans=pow(2*k+1,n-1,mod)*(k+x)
	ans%=mod
	if x>0:
		def mul(a,b):
			c=[[0]*x for _ in range(x)]
			for i in range(x):
				for j in range(x):
					for k in range(x):
						c[i][j]=(c[i][j]+a[i][k]*b[k][j])%mod
			return c
		def mpow(m,p):
			if p==0:return [[int(i==j) for i in range(x)] for j in range(x)]
			if p==1:return m
			half=mpow(m,p//2)
			full=mul(half,half)
			if p%2:full=mul(full,m)
			return full
		mat=[[0]*x for _ in range(x)]
		for i in range(x):
			for j in range(max(0,i-k),min(x,i+k+1)):
				mat[i][j]=1
		mat=mpow(mat,n-1)
		sub=sum(sum(r) for r in mat)
		ans-=sub
		ans%=mod
	print(ans)