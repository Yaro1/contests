import sys
import heapq

def brute_force(k, n, viewed_y, viewed_all):
    if k == n:
        return 1
    cnt = 0
    for i in range(0, n):
        if i not in viewed_y and (k, i) not in viewed_all:
            viewed_all_new = viewed_all.copy()
            for j in range(-10, 11):
                viewed_all_new.add((k+j, i+j))
                viewed_all_new.add((k+j, i-j))
            cnt += brute_force(k+1, n, viewed_y.union(set([i])), viewed_all_new)
    return cnt

def solution():
    n = int(sys.stdin.readline().split()[0])
    print(brute_force(0, n, set(), set()))
    

solution()