import sys
import math

def solution():
    n = int(sys.stdin.readline().split()[0])
    if n % 3 == 0:
        if (n - 5) % 3 == 1 and (n - 5) != 4 and (n - 5) != 1 and n - 5 > 0:
            print("YES")
            print(1, 4, n - 5)
        elif (n - 7) % 3 == 2 and (n - 7) != 5 and (n - 7) != 2 and n - 7 > 0:
            print("YES")
            print(2, 5, n - 7)
        else:
            print("NO")
    elif n % 3 == 1:
        if (n - 3) % 3 == 1 and (n - 3) != 1 and n - 3 > 0:
            print("YES")
            print(1, 2, n-3)
        else:
            print("NO")
    else:
        if (n - 3) % 3 == 2 and (n - 3) != 1 and (n - 3) != 2 and n - 3 > 0:
            print("YES")
            print(1, 2, n - 3)
        else:
            print("NO")




for _ in range(int(sys.stdin.readline().split()[0])):
    solution()