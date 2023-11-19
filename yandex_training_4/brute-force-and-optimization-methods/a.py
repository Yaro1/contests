import sys
import heapq

def brute_force(n, l, viewed):
    if len(l) == n: print(l)
    for i in range(1, n+1):
        if i not in viewed:
            brute_force(n, l+str(i), viewed.union(set([i])))

def solution():
    n = int(sys.stdin.readline().split()[0])
    brute_force(n, "", set())
    

solution()