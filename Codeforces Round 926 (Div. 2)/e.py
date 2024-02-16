from sys import stdin

def read_input():
    n = int(stdin.readline())
    tree = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = [int(w) - 1 for w in stdin.readline().split()]
        tree[a].append(b)
        tree[b].append(a)
    k = int(stdin.readline())
    pairs = []
    for i in range(k):
        pairs.append(tuple(int(w) - 1 for w in stdin.readline().split()))
    return tree, pairs

def solve(tree, pairs):
    n = len(tree)
    k = len(pairs)
    stack = [(None, 0, 0)]
    active_pairs = [0] * n
    for i , (a, b) in enumerate(pairs):
        active_pairs[a] ^= 1 << i
        active_pairs[b] ^= 1 << i
    edge_masks = []
    while stack:
        u, v, t = stack.pop()
        if t == 0:
            stack.append((u, v, 1))
            for w in tree[v]:
                if w == u:
                    continue
                stack.append((v, w, 0))
        else:
            mask = active_pairs[v]
            for w in tree[v]:
                if w == u:
                    continue
                mask ^= active_pairs[w]
            active_pairs[v] = mask
            if mask != 0:
                edge_masks.append(mask)
    edge_masks = list(set(edge_masks))
    # print(n, k, edge_masks)
    cnt_to_cover = [k] * (1 << k)
    cnt_to_cover[0] = 0
    for mask in range((1 << k)):
        for e_mask in edge_masks:
            cnt_to_cover[mask | e_mask] = min(
                cnt_to_cover[mask | e_mask],
                cnt_to_cover[mask] + 1
            )
    return cnt_to_cover[-1]


n_tests = int(stdin.readline())
for test_id in range(n_tests):
    print(solve(*read_input()))
