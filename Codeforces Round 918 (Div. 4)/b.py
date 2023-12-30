import sys
 
def solution():
    s = []
    for i in range(3):
        s.append(input().split()[0])
    s_good = set(["A", "B", "C"])
    for i in s:
        if "?" in i:
            res = s_good - set(i)
            print(res.pop())
            return

 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()