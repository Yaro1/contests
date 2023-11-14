import sys
import heapq

def dijkstra(graph, s, f):
    q, ancestors = [(0, s, 0)],  {}
    while len(q) > 0:
        arrive, curr_node, ancestor = heapq.heappop(q)
        if curr_node in ancestors:
            continue
        ancestors[curr_node] = (ancestor, arrive)
        for i in graph[curr_node]:
            if i[0] not in ancestors and arrive <= i[1]:
                heapq.heappush(q, (i[2], i[0], curr_node))
    return ancestors

def solution():
    n = int(sys.stdin.readline().split()[0])
    d, v = map(int, sys.stdin.readline().split())
    r = int(sys.stdin.readline().split()[0])
    graph = {i+1: [] for i in range(n)}
    for i in range(r):
        a, start_time, b, arrive_time = map(int, sys.stdin.readline().split())
        graph[a].append((b, start_time, arrive_time))
    result = dijkstra(graph, d, v)
    # print(result)
    print(result[v][1] if v in result else -1)
    

solution()