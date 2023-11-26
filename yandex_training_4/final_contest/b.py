import sys

def z_function(s):
    n = len(s)
    z = [0 for i in range(n)]
    i, l, r = 1, 0, 0
    while i < n:
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while (i + z[i] < n) and (s[z[i]] == s[i + z[i]]):
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
        i += 1
    return z

def solution():
    n = int(sys.stdin.readline().split()[0])
    s = sys.stdin.readline().split()[0]
    s_rev = s[::-1]
    a = z_function(s+s_rev)
    print(*a[::-1][:len(s)])

solution()


# B B A B B
# 1 2 0 1 5
# k = 1 1
# k = 2 
# k = 2
#  


# burannarub
# bbb -> ok + 1
# bua -> 0
# kkkaaakkk