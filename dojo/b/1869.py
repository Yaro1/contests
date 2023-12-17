import sys

def read(T=int):
	return [T(i) for i in sys.stdin.readline().split()]

def solve():
	n,k,a,b=read()
	x=[read() for i in range(n)]
	def dist(i,j):
		return abs(x[i][0]-x[j][0])+abs(x[i][1]-x[j][1])
	ans=dist(a-1,b-1)
	p,q=int(1e18),int(1e18)
	for i in range(k):
		p=min(p,dist(a-1,i))
		q=min(q,dist(b-1,i))
	print(min(p+q,ans))

def main():
	for i in range(read(int)[0]):
		solve()

main()