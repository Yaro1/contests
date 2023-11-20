import sys
    

def solution():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline()
    prefix_cnt_b = [0 for i in range(len(s))]
    prefix_cnt_a = [0 for i in range(len(s))]
    prefix_cnt_b[0] = 1 if s[0] == "B" else 0
    prefix_cnt_a[0] = 1 if s[0] == "A" else 0
    for i in range(1, len(s)):
        prefix_cnt_a[i] = prefix_cnt_a[i-1] + (1 if s[i] == "A" else 0)
        prefix_cnt_b[i] = prefix_cnt_b[i-1] + (1 if s[i] == "B" else 0)
    if prefix_cnt_b[-1] == k:
        print(0)
        return
    elif n == k:
        print(1)
        print(n, "B")
        return
    for i in range(n):
        cnt_a_a, cnt_a_b = 0, 0
        cnt_b_a, cnt_b_b = 0, 0
        cnt_a_a = prefix_cnt_b[i] + prefix_cnt_a[-1]
        cnt_a_b = prefix_cnt_b[-1] - prefix_cnt_b[i]
        cnt_b_a = prefix_cnt_a[-1] - prefix_cnt_a[i]
        cnt_b_b = prefix_cnt_a[i] + prefix_cnt_b[-1]
        if cnt_a_b == k:
            print(1)
            print(i+1, "A")
            return
        if cnt_b_b == k:
            print(1)
            print(i+1, "B")
            return
        

    

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()


# 6
# 5 4
# BBAAB
# 5 3
# AABAB