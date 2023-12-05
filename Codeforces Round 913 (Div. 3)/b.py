import sys

def solve():
    s = sys.stdin.readline().split()[0]
    big, small = [], []
    for num, i in enumerate(s):
        if i == 'b':
            if small:
                small.pop()
        elif i == 'B':
            if big:
                big.pop()
        elif i.isupper():
            big.append((num, i))
        elif i.lower():
            small.append((num, i))
    result = sorted(big + small, key=lambda x: x[0])
    result_str = [i[1] for i in result]
    print(''.join(result_str))


t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solve()