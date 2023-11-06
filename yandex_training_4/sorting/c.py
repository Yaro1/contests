import sys

def solution(a, b):
    result, i, j = [], 0, 0
    while i < len(a) or j < len(b):
        if i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            elif a[i] >= b[j]:
                result.append(b[j])
                j += 1
        elif i < len(a):
            result.append(a[i])
            i += 1
        elif j < len(b):
            result.append(b[j])
            j += 1
    return result

def read_array():
    n = int(sys.stdin.readline().split()[0])
    return [int(i) for i in sys.stdin.readline().split()]


a = read_array()
b = read_array()
print(' '.join(str(i) for i in solution(a, b)))