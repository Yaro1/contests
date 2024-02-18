import sys
import math
 
def solution():
    n, m = map(int, sys.stdin.readline().split())
    a = [int(i) % m for i in sys.stdin.readline().split()]
    s = input()
    a_numerated = []
    l, r = 0, len(a) - 1
    for i in range(len(s)):
        if s[i] == "L":
            a_numerated.append(a[l])
            l += 1
        else:
            a_numerated.append(a[r])
            r -= 1
    curr_mul = 1
    res = [a_numerated[-1]]
    for i in range(len(a_numerated) - 2, -1, -1):
        res.append((a_numerated[i] * res[-1]) % m)
    print(*res[::-1])

    
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()



# 3 1 4 2
# LRRL

# 3 1 4 2 2 4 1 3
# L R R L R L L R

# 3 2 4 1


# 6 8
# 1 2 3 4 5 6 6 5 4 3 2 1
# R L L L R R L L R R R L

# 6 8
# 2 3 4 6 2 1

# 6 8
# 1 5 6 5 4 3
