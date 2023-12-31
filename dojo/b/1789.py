for _ in range(int(input())):
    n=int(input())
    s = [x == '1' for x in input()]
    a = [i for i in range(n // 2) if s[i] != s[n-i-1]]
    if not a or max(a) - min(a) + 1 == len(a):
        print("Yes")
    else:
        print("No")
