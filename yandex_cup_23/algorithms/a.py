import sys
import heapq
 
n = int(sys.stdin.readline().split()[0])
arr = [int(i) for i in sys.stdin.readline().split()]
checks = [-1 for i in range(1000001)]
for i in range(len(arr)):
    checks[arr[i]] = i

cnt_checks = 0
for i in range(1, len(checks)):
    if checks[i] != -1 and checks[i] > checks[i - 1]:
        cnt_checks += 1
    else:
        break

print(cnt_checks)