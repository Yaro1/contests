import sys

def divisorGenerator(n):
    for i in range(1,n//2+1):
        if n%i == 0: yield i
    yield n
    

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in sys.stdin.readline().split()]
    a_pref_sum = [a[0]]
    for i in range(1, len(a)):
        a_pref_sum.append(a_pref_sum[-1] + a[i])
    
    max_diff = 0
    for div in divisorGenerator(n):
        local_max, local_min = float("-inf"), float("inf")
        for j in range(div-1, len(a), div):
            minus = a_pref_sum[j - div] if j - div >= 0 else 0
            value = a_pref_sum[j] - minus
            local_max = max(local_max, value)
            local_min = min(local_min, value)
        max_diff = max(max_diff, local_max - local_min)
    print(max_diff)
    
    
    

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()


# 10 2 3 6 1 3
# 10 12 15 21 22 25