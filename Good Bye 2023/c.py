import sys


def solution():
    n = int(sys.stdin.readline().split()[0])
    a = [int(i) for i in input().split()]
    result = [a[0]]
    cnt_odd = 1 if a[0] % 2 != 0 else 0
    cnt_even = 1 if a[0] % 2 == 0 else 0
    curr_sum = a[0]
    for i in range(1, len(a)):
        curr_sum += a[i]
        if a[i] % 2 == 0:
            cnt_even += 1
        else:
            cnt_odd += 1
        if cnt_odd <= 2:
            substracting = cnt_odd % 2
        else:
            substracting = cnt_odd // 3
            if cnt_odd % 3 == 1:
                substracting += 1
        result.append(curr_sum - substracting)
    print(*result)

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()



# a b
# b_i -> b_j -> |a| + 1 |b| - 2 res = sum
# b_i -> a_j -> |b| - 1 |a| res = (sum - 1)
# a_i -> a_j -> |a| - 1 res = sum

# a=0 b=6
# a=1 b=4
# a=0 b=4
# a=1 b=2
# a=0 b=2
# a=1

# a=0 b=4
# a=1 b=2
# a=1 b=1
# a=1 b=0

# a=0 b=5
# a=1 b=3
# a=1 b=2
# a=2 b=0
# a=1 b=0