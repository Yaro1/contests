for i in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	x=a.count(0)
	y=a.count(1)
	z=n-x-y
	if x<=(n+1)//2:
		print(0)
	else:
		if 0<z or n==x: print(1)
		else: print(2)