import heapq 
 
 
def read_adj_list(N: int, K: int): 
    adjacency_list = [[] for _ in range(N + 1)] 
    for i in range(K): 
        a, b, t, w = map(int, input().split()) 
        adjacency_list[a].append((b, t, w)) 
        adjacency_list[b].append((a, t, w)) 
    return adjacency_list 
 
 
def task_c(): 
    N, M = map(int, input().split()) 
    adj_list = read_adj_list(N, M) 
     
    left = 0 
    right = 10000000 
    while left <= right: 
        mid = (right + left) // 2 
 
 
        mass = 3000000 + mid * 100 
        dist = [1441 for _ in range(N + 1)] 
        dist[1] = 0 
        q = [] 
        heapq.heappush(q, (dist[1], 1)) 
 
        while len(q) > 0: 
            min_v = heapq.heappop(q)[1] 
            if min_v == N: break
            for k in adj_list[min_v]: 
                if dist[k[0]] > dist[min_v] + k[1] and mass <= k[2]: 
                    dist[k[0]] = dist[min_v] + k[1] 
                    heapq.heappush(q, (dist[k[0]], k[0])) 
 
        if dist[N] <= 1440: 
            left = mid + 1 
        else: 
            right = mid - 1 
 
             
    if right < 0: 
        right = 0 
    print(right)     
     
     
task_c()