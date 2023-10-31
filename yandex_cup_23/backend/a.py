import sys
 
n, m = sys.stdin.readline().split()
n, m = int(n), int(m)
a = [int(i) for i in sys.stdin.readline().split() if i != "0"]
if len(a) == 0:
    print(0)
else:
    a_suff_sum = [0 for i in range(len(a))]
    a_suff_sum[0] = a[0]
    for i in range(1, len(a)):
        a_suff_sum[i] = a_suff_sum[i - 1] + a[i]
    result = 0
    for i in range(len(a) - 1):
        index_value = min(len(a) - 1, i + a[i])
        value = a[i]*a[i] + (a_suff_sum[index_value] - a_suff_sum[i])
        result += value
    result += a[-1]*a[-1]
    print(result)