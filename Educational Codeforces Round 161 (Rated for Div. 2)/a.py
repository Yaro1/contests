import sys

def solution():
    n = int(input())
    a = input()
    b = input()
    c = input()
    answer = []
    for i in range(n):
        if c[i].islower():
            if a[i] == c[i] or b[i] == c[i]:
                answer.append(False)
            else:
                answer.append(True)
        else:
            if a[i] == lower(c[i]) or b[i] == lower(c[i]):
                answer.append(False)
            else:
                answer.append(True)
    print("YES" if any(answer) else "NO")
    

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
        