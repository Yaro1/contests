for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    elif n % 2:
        print(-1)
    else:
        print(*(i + 1 if i % 2 else i - 1 for i in range(1, n + 1)))