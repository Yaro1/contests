import sys

def solution(a):
    pref, suff = [0 for i in range(len(a))], [0 for i in range(len(a))]
    pref[0] = a[0]
    for i in range(1, len(a)):
        pref[i] = pref[i - 1] + a[i]
    suff[-1] = a[-1]
    for i in range(len(a) - 2, -1, -1):
        suff[i] = suff[i + 1] + a[i]
    for i in range(len(a)):
        if 0 < i < len(a) - 1:
            left = a[i] * i - pref[i - 1]
            right = suff[i + 1] - a[i] * (len(a) - i - 1)
            a[i] = left + right
        elif i == 0:
            a[i] = suff[i + 1] - (a[i]*(len(a) - 1))
        else:
            a[i] = (a[i]*(len(a) - 1)) - pref[i - 1]
    print(' '.join(str(i) for i in a))


n = int(sys.stdin.readline()[0])
a = [int(i) for i in sys.stdin.readline().split()]
solution(a)