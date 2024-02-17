import sys
import math
 
def solution():
    n = int(sys.stdin.readline().split()[0])
    nums = list(range(1, n + 1))
    res = []
    i, j = 0, n - 1
    while i <= j:
        if len(res) % 2 == 0:
            res.append(nums[j])
            j -= 1
        else:
            res.append(nums[i])
            i += 1
    print(*res)
    
            




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
