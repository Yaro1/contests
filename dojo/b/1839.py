for __ in range(int(input())):
    n = int(input())
    bulbs = dict()
    ans = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x not in bulbs:
            bulbs[x] = list()
        bulbs[x].append(y)
    for k in bulbs:
        ans += sum(sorted(bulbs[k])[-k:])
    print(ans)
