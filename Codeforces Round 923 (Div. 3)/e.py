for _ in range(int(input())):
    n,k = map(int,input().split())

    ans = [0 for i in range(n)]

    x = n; y = 1
    for i in range(k):
        for j in range(i,n,k):
            if i%2 == 0:
                ans[j] = x
                x -= 1
            else:
                ans[j] = y
                y += 1
    print(*ans)
