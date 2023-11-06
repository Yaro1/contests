import sys

def predicat(l, i, j, f):
    cnt = 0
    for k in range(i, j + 1):
        if f(l[k]):
            cnt += 1
    return cnt



n = int(sys.stdin.readline().split()[0])
a = [float(i) for i in sys.stdin.readline().split()]
x = float(sys.stdin.readline().split()[0])
cnt_left = predicat(a, 0, len(a) - 1, lambda value: value < x)
cnt_right = len(a) - cnt_left
print(cnt_left)
print(cnt_right)