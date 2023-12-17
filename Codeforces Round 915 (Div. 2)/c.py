import sys
from collections import deque

def solve():
    n = int(sys.stdin.readline().split()[0])
    s = list(sys.stdin.readline().split()[0])
    if s == sorted(s):
        print(0)
        return
    stack = [(s[0], 0)]
    for i in range(1, len(s)):
        while stack and s[i] > stack[-1][0]:
            stack.pop()
        stack.append((s[i], i))

    stack_char = [i[0] for i in stack]
    stack_indexes = deque([i[1] for i in stack])

    m_value = max(stack_char)
    finishing = 0
    for i in range(len(stack_char)):
        if stack_char[i] == m_value:
            finishing = i
        else:
            break
    answer = len(stack) - 1 - finishing
    cnt_values = answer
    start_idx = 0

    while stack_char:
        for i in range(start_idx+1, stack_indexes[0]):
            if s[i] < s[i - 1]:
                print(-1)
                return
        value_char = stack_char.pop()
        value_idx = stack_indexes.popleft()
        start_idx = value_idx - 1
        s[value_idx] = value_char
    print(answer)
    


t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solve()


# 20 5 1 4 2
# 1 2 4 5 20
# 1 3 7 12 32