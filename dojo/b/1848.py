for _ in range(int(input())):
	n, k = map(int, input().split())
	c = list(map(int, input().split())) 
	arr = [list() for j in range(k+1)]
 
	for i in range(n):
		arr[c[i]].append(i)
 
	ans = n
 
	for v in arr[1:]:
		v.append(n)
		first = second = 0
		last = -1
		for i in v:
			d = i - last
			if d > first:
				second = first
				first = d
			elif d > second:
				second = d
			last = i
		ans = min(ans, max(second, (first+1)//2))
	print(ans-1)