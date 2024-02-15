import sys
import math
 
def solution():
    n, k = map(int, sys.stdin.readline().split())
    full_diag = 4*n - 2
    if k <= full_diag - 2:
        print(math.ceil(k / 2))
    elif k == full_diag - 1:
        print(math.ceil((k - 1) / 2) + 1)
    else:
        print(math.ceil((k - 2) / 2) + 2)
            




t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()

# 4n - 2 = 14

# 1 1 1 1
# 0 0 0 0
# 0 0 0 0
# 0 1 1 0


# 1 1 1 1 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 1 1 1 0
