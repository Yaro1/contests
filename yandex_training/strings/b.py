import sys


def prefix_function(s):
    pi = [0 for i in range(len(s))]
    for i in range(1, len(s)):
        j = pi[i - 1]
        while s[i] != s[j] and j > 0:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def solution(s):
    pref = prefix_function(s)
    print(pref)
    i = len(pref) - 1
    while i > -1:
        if i < len(pref) - 1 and pref[i] == pref[i + 1]:
            while i > -1 and pref[i] == pref[i + 1]:
                i -= 1
            print(i + 2)
            return
        if i > -1 and pref[i] == 0:
            print(i + 1)
            return
        i -= 1

s = sys.stdin.readline().split()[0]
solution(s)