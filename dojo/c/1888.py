from collections import Counter

def solve():
	n = int(input())
	a = [int(_) for _ in input().split()]

	st = set()
	cnt = Counter(a)
	dist = len(cnt)	
	anw = 0
	  
	for v in a:
		if v not in st:
			anw += dist

		st.add(v)	

		cnt[v] -= 1
		if cnt[v] == 0:
			dist -= 1

	print(anw)			

def main():
	t = int(input())
	while t > 0:
		t -= 1
		solve()

if __name__ == '__main__':
	main()