T = int(input())

def solve():
	n = int(input())
	a = list(map(int, input().split()))
	a = sorted(a)
	ans = 0
	s = 0
	for i in range(n):
		if i > 0 and a[i] != a[i - 1]:
			s = 0
		ans += s
		s += i
	print(ans)

for _ in range(T):
	solve()