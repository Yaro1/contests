import sys

def solution(a, b, c):
    l = sorted([a, b, c])
    print("YES") if l[0] + l[1] > l[2] else print("NO")

a = int(sys.stdin.readline().split()[0])
b = int(sys.stdin.readline().split()[0])
c = int(sys.stdin.readline().split()[0])
solution(a, b, c)