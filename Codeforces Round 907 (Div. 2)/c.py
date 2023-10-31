import sys

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = sorted([int(i) for i in sys.stdin.readline().split()])
    cnt, i, j, x = 0, 0, len(a) - 1, 0
    while i < j:
        if x + a[i] < a[j]:
            cnt += a[i]
            x += a[i]
            a[i] = 0
            i += 1
        elif x + a[i] == a[j]:
            cnt += (a[i] + 1)
            x = 0
            a[i] = 0
            a[j] = 0
            i += 1
            j -= 1
        else:
            value = a[j] - x
            cnt += (value + 1)
            x = 0
            a[j] = 0
            j -= 1
            a[i] -= value
    if i == j and a[i] > 0:
        if a[i] == 1:
            cnt += 1
        else:
            if x >= a[i]:
                cnt += 1
            else:
                value = (a[i] - x + 1) // 2
                cnt += value + 1
    print(cnt)



    

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()