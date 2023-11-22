import sys
import math

def solution():
    n = int(sys.stdin.readline().split()[0])
    a = list(map(int, sys.stdin.readline().split()))
    m_value, flag = a[0], False
    curr_value = a[0]
    for i in range(1, len(a)):
        if a[i] >= a[i - 1]:
            curr_value = a[i]
        else:
            m_value = max(m_value, curr_value)
            flag = True
            curr_value = a[i]
    if flag:
        print(m_value)
    else:
        print(0)



for _ in range(int(sys.stdin.readline().split()[0])):
    solution()