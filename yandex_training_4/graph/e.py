import sys
import heapq
from collections import defaultdict, OrderedDict
import copy
from functools import lru_cache

def solution():
    n = int(sys.stdin.readline().split()[0])
    yamchiki = []
    for _ in range(n):
        yamchiki.append([int(i) for i in sys.stdin.readline().split()])
    distances = {i:{i:0} for i in range(1, n+1)}
    for _ in range(n - 1):
        a, b, dist = map(int, sys.stdin.readline().split())
        distances[a][b] = dist
        distances[b][a] = dist
    paths = {i:{i:True} for i in range(1, n+1)}
    new_distances = {i: {} for i in range(1, n+1)}
    for i in distances:
        for j in distances[i]:
            new_distances[i][j] = distances[i][j]
    new_distances[-1] = {}

    def lookup(distances, node):
        q = [(node, -1)]
        viewed = set()
        while q:
            curr_node, ancestor = q.pop()
            # print(curr_node)
            viewed.add(curr_node)
            # if ancestor != 1:
            #     for somebody in set(new_distances[ancestor]) - set(new_distances[curr_node]):
            #         new_distances[somebody][curr_node] = distances[curr_node][ancestor] + new_distances[ancestor][somebody]
            #         new_distances[curr_node][somebody] = distances[curr_node][ancestor] + new_distances[ancestor][somebody]
            for somebody in set(new_distances[ancestor]) - set(new_distances[curr_node]):
                new_distances[somebody][curr_node] = distances[curr_node][ancestor] + new_distances[ancestor][somebody]
                new_distances[curr_node][somebody] = distances[curr_node][ancestor] + new_distances[ancestor][somebody]
            for j in distances[curr_node]:
                if j not in viewed:
                    q.append((j, curr_node))

        

    def finder_one_more(s):
        results = {i:float("inf") for i in range(1, n+1)}
        to_view = set([i for i in range(1, n+1)])
        parents = {i: -1 for i in range(1, n + 1)}
        results[s] = 0
        q = [(0, s)]
        # q = OrderedDict()
        # q[(0, s)] = 1
        while q:
            curr_path, curr_node = heapq.heappop(q)
            # k, v = q.popitem()
            # curr_path, curr_node = k[0], k[1]
            if curr_path > results[curr_node]: # 24.file - 6k repeats, 25.file - 295374 repeats
                continue
            to_view.remove(curr_node)
            # dijkstra(distances, curr_node)
            for j in to_view:
                l = new_distances[j][curr_node] / yamchiki[j - 1][1] + yamchiki[j - 1][0]
                if results[curr_node] + l < results[j]:
                    results[j] = results[curr_node] + l
                    parents[j] = curr_node
                    heapq.heappush(q, (results[j], j))
                    # if (results[j], j) in q:
                    #     q.pop((results[j], j))
                    # results[j] = results[curr_node] + l
                    # q[(results[j], j)] = 1
        return results, parents

    lookup(distances, 1)
    to_each, parents = finder_one_more(1)
    # print(to_each)
    # print(parents)
    baddest_result = max(to_each.values())
    print(baddest_result)
    for i in to_each:
        if to_each[i] == baddest_result:
            path = [i]
            while parents[path[-1]] != -1:
                path.append(parents[path[-1]])
            print(*path)
            return
    

solution()



# 1

# 4
# 1 1
# 10 30
# 5 40
# 1 10
# 1 2 300
# 1 3 400
# 2 4 100

# Res
# 31.0000000000
# 4 2 1


# 2

# 3
# 1 1
# 0 10
# 0 55
# 1 2 100
# 2 3 10

# Res
# 3.0000000000
# 2 3 1

