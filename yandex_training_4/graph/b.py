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
            return ancestors
        for i in graph[curr_node]:
            if i[1] not in ancestors:
                heapq.heappush(q, (curr_path+i[0], i[1], curr_node))
    return -1

def solution():
    n, s, f = map(int, sys.stdin.readline().split())
    graph = {i: [] for i in range(n)}
    for i in range(n):
        l = [int(i) for i in  sys.stdin.readline().split()]
        for j in range(len(l)):
            if l[j] != 0 and l[j] != -1:
                if i in graph:
                    graph[i].append((l[j], j))
    result = dijkstra(graph, s-1, f-1)
    if result == -1:
        print(-1)
    else:
        # print(result)
        path = [f-1]
        while path[-1] != s-1:
            path.append(result[path[-1]][0])
        print(*[i + 1 for i in path[::-1]])
    

solution()