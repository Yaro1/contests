import sys

def max_sum(a):
    max_so_far = float("-inf")
    max_ending_here = 0
      
    for i in range(0, len(a)):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far
    

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in sys.stdin.readline().split()]
    second = 1
    s = float("-inf")
    bucket = [a[0]]
    while second < len(a):
        if ((a[second] % 2) != (a[second - 1] % 2)):
            bucket.append(a[second])
            second += 1
        else:
            s = max(s, max_sum(bucket))
            bucket = [a[second]]
            second += 1
    s = max(s, max_sum(bucket))
    print(s)
            
    
    
    

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()


# 10 2 3 6 1 3
# 10 12 15 21 22 25