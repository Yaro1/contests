import sys

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    a = sorted([(a[i], i) for i in range(len(a))], reverse=True)
    b = sorted([(b[i], i) for i in range(len(b))], reverse=True)
    c = sorted([(c[i], i) for i in range(len(c))], reverse=True)
    value_max = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if a[i][1] == b[j][1] or a[i][1] == c[k][1] or b[j][1] == c[k][1]:
                    continue
                value_max = max(value_max, a[i][0] + b[j][0] + c[k][0])
    print(value_max)
    



t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
        