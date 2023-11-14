import sys
import heapq

def dijkstra(graph, s, f):
    q, viewed = [(0, s)], set()
    while len(q) > 0:
        curr_path, curr_node = heapq.heappop(q)
        if curr_node == f:
            return curr_path
        viewed.add(curr_node)
        for i in graph[curr_node]:
            if i not in viewed:
                heapq.heappush(q, (curr_path+i[1], i[0]))
    return -1

def solution():
    n, s, f = map(int, sys.stdin.readline().split())
    graph = {i: [] for i in range(n)}
    for i in range(n):
        l = [int(i) for i in  sys.stdin.readline().split()]
        for j in range(len(l)):
            if l[j] != 0 and l[j] != -1:
                if i in graph:
                    graph[i].append((j, l[j]))
    print(dijkstra(graph, s-1, f-1))
    

solution()