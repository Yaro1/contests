import sys

def solution():
    a = int(sys.stdin.readline().split()[0])
    b = int(sys.stdin.readline().split()[0])
    n = int(sys.stdin.readline().split()[0])
    value = b // n if b % n == 0 else b // n + 1
    if a <= value:
        print("No")
    else:
        print("Yes")


solution()