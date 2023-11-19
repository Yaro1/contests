import sys
from collections import defaultdict

def powerset(seq, s, graph, nodes_sum):
    if len(seq) <= 1:
        yield seq, s
    else:
        new_seq = seq[1:]
        helper = sum(graph[node][seq[0]] for node in new_seq)
        new_s = s - (nodes_sum[seq[0]] - helper) + helper
        for item, item_s in powerset(new_seq, new_s, graph, nodes_sum):
            helper = sum(graph[node][seq[0]] for node in item)
            item_s_additional = item_s + (nodes_sum[seq[0]] - helper) - helper
            yield [seq[0]]+item, item_s_additional
            yield item, item_s

def check(graph, n1, s, nodes_sum):
    m_weight = 0
    m_n1 = None
    ind = 1
    for curr_n1, weight in powerset(n1, 0, graph, nodes_sum):
        if ind == 262145: break # we need in only one half of powerset from n1
        if weight > m_weight:
            m_weight = weight
            m_n1 = curr_n1
        ind += 1
    return m_weight, m_n1
    
    

            

def solution():
    n = int(sys.stdin.readline().split()[0])
    graph = []
    s = 0
    nodes_sum = {}
    for i in range(n):
        a = list(map(int, sys.stdin.readline().split()))
        s_a = sum(a)
        s += s_a
        nodes_sum[i] = s_a
        graph.append(a)
    s //= 2
    result, n1 = check(graph, [i for i in range(n)], s, nodes_sum)
    print(result)
    print(*[1 if i in n1 else 2 for i in range(len(graph))])
    

solution()