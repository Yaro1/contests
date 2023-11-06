import sys

def solution(l):
    l_new = [[0 for i in range(len(l[0]))] for j in range(len(l))]
    for i in range(len(l)):
        for j in range(len(l[0])):
            l_new[i][j] = l[i][j]
    for i in range(1, len(l)):
        for j in range(1, len(l[0])):
            if l_new[i][j] == 1 and (l_new[i - 1][j] > 0) and (l_new[i][j - 1] > 0) and (l_new[i - 1][j - 1] > 0):
                l_new[i][j] = min(l_new[i - 1][j], l_new[i][j - 1], l_new[i - 1][j - 1]) + 1
    print(max([max(i) for i in l_new]))


n, m = map(int, sys.stdin.readline().split())
l = []
for _ in range(n):
    l.append([int(i) for i in sys.stdin.readline().split()])
solution(l)