import sys
 
def solution():
    s = []
    for i in range(3):
        s.append(input().split()[0])
    s = set(["A", "B", "C"])
    for i in s:
        if "?" in i:
            res = s - set(i)
            print(s.pop())
            return

 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()