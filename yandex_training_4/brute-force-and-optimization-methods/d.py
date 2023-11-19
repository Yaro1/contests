import sys
from collections import defaultdict

# now + min(E)*k >= best -> cut
# now + s(min_ed {i where i not in now_e})
# from min ocenka minus min rebro from viewed node

def solution():
    n = int(sys.stdin.readline().split()[0])
    graph, checking = [], 0
    global best
    best = float("inf")

    def finder(graph, curr_node, curr_path, path_len):
        global best
        if len(curr_path) == len(graph) and curr_node == 0:
            best = min(best, path_len)
            return best
        if len(curr_path) == len(graph) and graph[curr_node][0] == 0:
            return float("inf")
        for i in range(len(graph[curr_node])):
            if ((i == 0 and len(curr_path) == len(graph)) or i not in curr_path) and graph[curr_node][i] != 0:
                value = finder(graph, i, curr_path.union(set([i])), path_len + graph[curr_node][i])
                best = min(value, best)
        return best

    for i in range(n):
        a = list(map(int, sys.stdin.readline().split()))
        checking += min(a)
        graph.append(a)
    
    result = finder(graph, 0, set([0]), 0)
    print(result if result != float("inf") else -1)
    

solution()