import sys

def str2dict(s):
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    return d

def solution(s1, s2):
    d1, d2 = str2dict(s1), str2dict(s2)
    if d1 == d2:
        print("YES")
    else:
        print("NO")


s1, s2 = sys.stdin.readline(), sys.stdin.readline()
solution(s1, s2)