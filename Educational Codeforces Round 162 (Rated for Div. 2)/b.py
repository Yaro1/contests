import sys

def solution():
	n, k = map(int, sys.stdin.readline().split())
	x = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	monsters = [[abs(i), j] for i, j in zip(a, x)]
	monsters.sort(key=lambda x: x[0])
	step = 0
	curr_k = k
	for i in range(len(monsters)):
		while monsters[i][1] > 0:
			if monsters[i][0] - step == 0:
				print("NO")
				return
			if curr_k >= monsters[i][1]:
				curr_k -= monsters[i][1]
				monsters[i][1] = 0
			else:
				monsters[i][1] -= curr_k
				curr_k = k
				step += 1
	print("YES")
		



        
    

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
        