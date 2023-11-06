import sys

def merge(a, l1, r1, l2, r2):
    result, i, j = [], l1, l2
    while i < r1 + 1 or j < r2 + 1:
        if i < (r1 + 1) and j < (r2 + 1):
            if a[i] < a[j]:
                result.append(a[i])
                i += 1
            elif a[i] >= a[j]:
                result.append(a[j])
                j += 1
        elif i < (r1 + 1):
            result.append(a[i])
            i += 1
        elif j < (r2 + 1):
            result.append(a[j])
            j += 1
    k = 0
    for i in range(l1, r2 + 1):
        a[i] = result[k]
        k += 1
        

# 0 5 -> (0, 2) (3, 5)
# 0 2 -> (0, 1) (2, 2)
# 0 1 -> (0, 0) (1, 1)

def merge_sort(a, l, r):
    if l < r:
        merge_sort(a, l, (l+r) // 2)
        merge_sort(a, (l+r) // 2 + 1, r)
        merge(a, l, (l+r) // 2, (l+r) // 2 + 1, r)
    return a
    
    

def read_array():
    n = int(sys.stdin.readline().split()[0])
    return [int(i) for i in sys.stdin.readline().split()]


a = read_array()
print(' '.join(str(i) for i in merge_sort(a, 0, len(a) - 1)))