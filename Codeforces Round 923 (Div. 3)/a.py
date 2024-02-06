import sys
 
def solution():
    n = int(sys.stdin.readline().split()[0])
    s = input()
    l, r = None, None
    for num, i in enumerate(s):
        if i == "B" and l is None:
            l = num
        elif i == "B" and l is not None:
            r = num
    if r is None and l is not None:
        print(1)
    elif r is None and l is None:
        print(0)
    else:
        print(r - l + 1)
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()