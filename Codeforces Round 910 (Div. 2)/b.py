from math import ceil
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    x = arr[n-1]
    for i in range(n-2, -1, -1):
        omg = ceil(arr[i]/x)
        res += (omg-1)
        x = arr[i]//omg
    print(res)