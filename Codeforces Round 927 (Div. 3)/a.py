import sys
 
def solution():
    n = int(sys.stdin.readline().split()[0])
    s = input()
    res = 0
    i = 0
    while i < len(s):
        if s[i] == '@':
            res += 1
            i += 1
        elif s[i] == '.':
            i += 1
        else:
            if i + 1 < len(s) and s[i + 1] != '*':
                i += 1
            else:
                break
    print(res)
    
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
