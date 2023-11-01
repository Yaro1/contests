import sys

def delimeters(f, s):
    for i in range(2, 100*100):
        while f % i == 0 and s % i == 0:
            f = f // i
            s = s // i
    return f, s

a, b, c, d = map(int, sys.stdin.readline().split())
up = a * d + c * b
down = b * d
res_up, res_down = delimeters(up, down)
print(res_up, res_down)
