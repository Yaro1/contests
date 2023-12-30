for _ in range(int(input())):
	n = int(input())
	d = []
	for i in range(n):
		a,b = map(int, input().split())
		d.append((a,b))
	d.sort()
	arr = [j for i,j in d]
	b = sorted(arr)
	N = n
	ans = 0
	for i in range(n-1, -1, -1):
		I = 0
		J = N-1
		while I<J:
			M = (I+J)//2
			if b[M]>arr[i]:
				J = M - 1
			elif b[M]<arr[i]:
				I = M + 1
			else:
				I = M
				break
		del b[I]
		ans += N-I-1
		N-=1
	print(ans)