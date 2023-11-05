import sys
import math


def palindrom_finder_nechet(s):
    l, r = 0, -1
    d = [0 for i in range(len(s))]
    for i in range(1, len(s)):
        k = 0
        if i <= r:
            k = min(r - i, d[r - i + l])
        while i + k + 1 < len(s) and i - k - 1 >= 0 and s[i + k + 1] == s[i - k - 1]:
            k += 1
        d[i] = k
        if i + k > r:
            l = i - k
            r = i + k
    return d


def palindrom_finder_chet(s):
    l, r = 0, -1
    d = [0 for i in range(len(s))]
    for i in range(1, len(s)):
        k = 0
        if i <= r:
            k = min(r - i + 1, d[r - i + l + 1])
        while i + k < len(s) and i - k - 1 >= 0 and s[i+k] == s[i - k - 1]:
            k += 1
        d[i] = k
        if i + k - 1 > r:
            l = i - k
            r = i + k - 1
    return d

def solution(a):
    answer = []
    res_chet, res_nechet = palindrom_finder_chet(a), palindrom_finder_nechet(a)
    cnt_chet, cnt_nechet = 0, 0
    # print(res_chet, res_nechet)
    for i in range(len(res_chet)):
        if res_chet[i] > 0:
            cnt_chet += res_chet[i]
    
    for i in range(len(res_nechet)):
        if res_nechet[i] > 0:
            cnt_nechet += res_nechet[i]
        
    print(len(a) + cnt_chet + cnt_nechet)



a = sys.stdin.readline().split()[0]
solution(a)