import sys
import heapq

def dijkstra(graph, s, f):
    q, ancestors = [(0, s, -1)],  {}
    while len(q) > 0:
        curr_path, curr_node, ancestor = heapq.heappop(q)
        if curr_node in ancestors:
            continue
        ancestors[curr_node] = (ancestor, curr_path)
        if curr_node == f:
            return curr_path
        for i in graph[curr_node]:
            if i[1] not in ancestors:
                heapq.heappush(q, (curr_path+i[0], i[1], curr_node))
    return -1

def solution():
    n, k = map(int, sys.stdin.readline().split())
    graph = {i+1: [] for i in range(n)}
    for i in range(k):
        a, b, l = map(int, sys.stdin.readline().split())
        graph[a].append((l, b))
        graph[b].append((l, a))
    s, f = map(int, sys.stdin.readline().split())
    print(dijkstra(graph, s, f))
    

solution()