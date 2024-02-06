import sys
 
def solution():
    n, m, k = map(int, sys.stdin.readline().split())
    a = [int(i) for i in sys.stdin.readline().split()]
    b = [int(i) for i in sys.stdin.readline().split()]
    if (len(a) < (k // 2)) or (len(b) < (k // 2)):
        print("NO")
        return
    a_set, b_set = set([i for i in a if 1 <= i <= k]), set([i for i in b if 1 <= i <= k])
    a_b = a_set - b_set
    b_a = b_set - a_set
    if (len(a_b) > (k // 2)) or (len(b_a) > (k // 2)):
        print("NO")
        return
    checking = set([i for i in range(1, k+1)])
    if len(checking - (a_set.union(b_set))) > 0:
        print("NO")
        return
    print("YES")

    
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()