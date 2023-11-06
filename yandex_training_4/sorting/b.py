import sys

import random

def quick_sort(xs, fst, lst):
    if fst >= lst:
        return

    i, j = fst, lst
    pivot = xs[random.randint(fst, lst)]

    while i <= j:
        while xs[i] < pivot:
            i += 1
        while xs[j] > pivot:
            j -= 1

        if i <= j:
            xs[i], xs[j] = xs[j], xs[i]
            i, j = i + 1, j - 1
    quick_sort(xs, fst, j)
    quick_sort(xs, i, lst)


n = int(sys.stdin.readline().split()[0])
if n > 0:
    a = [int(i) for i in sys.stdin.readline().split()]
    quick_sort(a, 0, len(a) - 1)
    print(' '.join(str(i) for i in a))