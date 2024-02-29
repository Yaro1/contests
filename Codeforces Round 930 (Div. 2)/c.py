t = int(input())
for yty in range(t):
    n = int(input())
    idx = 0
    for i in range(1, n):
        print('?', idx, idx, i, i)
        a = input()
        if a == '<':
            idx = i
    ans = 0
    V = [0]
    for i in range(1, n):
        print('?', ans, idx, i, idx)
        a = input()
        if a == '<':
            ans = i
            V = [i]
        elif a == '=':
            V.append(i)
    g = len(V)
    ans = V[0]
    for i in range(1, g):
        print('?', ans, ans, V[i], V[i])
        a = input()
        if a == '>':
            ans = V[i]
    print('!', idx, ans)
