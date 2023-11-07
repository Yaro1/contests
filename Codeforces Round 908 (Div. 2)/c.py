for t in range(int(input())):
	n,k = map(int, input().split())
	b = list(map(int, input().split()))
	flag = True
	index = -1
	for i in range(min(n, k)):
		current = b[index]
		if current > n:
			flag = False
			break
		index = (index - current) % n
	if flag:
		print("Yes")
	else:
		print("No")