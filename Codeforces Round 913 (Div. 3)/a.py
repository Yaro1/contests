import sys

def solve():
    s = sys.stdin.readline().split()[0]
    letter, number = s[0], int(s[1])
    letters = list('abcdefgh')
    for i in letters:
        if i != letter:
            print(f"{i}{number}")
    for i in range(1, 9):
        if i != number:
            print(f"{letter}{i}")

t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solve()
        

        