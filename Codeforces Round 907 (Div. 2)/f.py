import sys
input = sys.stdin.readline

class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.data = [0] * n
    
    def update(self, idx, x):
        while idx < self.size:
            self.data[idx] += x
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x += self.data[end - 1]
            end &= end - 1
        return x
 

def solve():
    q = int(input())
    n = 1
    G = [[] for _ in range(q + 1)]
    todo = []

    for _ in range(q):
        t, *query = map(int, input().split())
        if t == 1:
            v = query[0] - 1
            G[v].append(n)
            todo.append((-1, n))
            n += 1

        else:
            v, x = query
            v -= 1
            todo.append((v, x))


    first = [-1] * n
    last = [-1] * n
    m = 0
    stack = [~0, 0]

    while stack:
        u = stack.pop()
        if u >= 0:
            first[u] = m
            m += 1

            for v in G[u]:
                stack.append(~v)
                stack.append(v)
        else:
            last[~u] = m
            m += 1


    ft = FenwickTree(m + 1)
    # add to entire subtree. To correct when new node is created, remove value to the subtree
    for v, x in todo:
        if v == -1:
            i = first[x]
            curr = ft.query(i + 1)
            
            ft.update(i, -curr)
            ft.update(i + 1, curr)

        else:
            l = first[v]
            r = last[v]
            ft.update(l, x)
            ft.update(r, -x)

    res = [0] * n
    for i, f in enumerate(first):
        res[i] = ft.query(f + 1)
    
    return " ".join(map(str, res))


T = int(input())
out = [solve() for _ in range(T)]
print("\n".join(map(str, out)))