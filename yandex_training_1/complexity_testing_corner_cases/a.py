import sys
 
def solution(a, b, c):
    if c == "freeze":
        if a > b:
            print(b)
        else:
            print(a)
    elif c == "heat":
        if a < b:
            print(b)
        else:
            print(a)
    elif c == "auto":
        print(b)
    elif c == "fan":
        print(a)
 
t_room, t_cond = map(int, sys.stdin.readline().split())
working_type = sys.stdin.readline().split()[0]
solution(t_room, t_cond, working_type)