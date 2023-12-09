import sys

def solve():
    a, b = map(int, sys.stdin.readline().split())
    x_k, y_k = map(int, sys.stdin.readline().split())
    x_q, y_q = map(int, sys.stdin.readline().split())
    if a != b:
        opportunities = [
            (a, b), (a, -b), (-a, b), (-a, -b), 
            (b, a), (b, -a), (-b, a), (-b, -a)
        ]
    else:
        opportunities = [
            (a, b), (a, -b), (-a, b), (-a, -b), 
        ]
    s_k = set()
    s_q = set()
    for item in opportunities:
        s_k.add((x_k + item[0], y_k + item[1]))
        s_q.add((x_q + item[0], y_q + item[1]))
    print(len(s_k.intersection(s_q)))

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solve()
        

        