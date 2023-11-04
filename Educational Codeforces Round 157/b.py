import sys
 
def manhatten_distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])
 
def solution():
    n = int(sys.stdin.readline().split()[0])
    a = sorted([int(i) for i in sys.stdin.readline().split()])
    points = []
    for i in range(0, len(a) // 2, 1):
        points.append((a[i], a[len(a) // 2 + i]))
    points.sort(key=lambda x: (x[0], x[1]))
    res = 0
    for i in range(1, len(points)):
        res += manhatten_distance(points[i], points[i - 1])
    print(res)
    for i in range(len(points)):
        print(points[i][0], points[i][1])
    
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()