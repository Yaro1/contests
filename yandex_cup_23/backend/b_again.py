import sys

def bisect_left(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < x: lo = mid + 1
        else: hi = mid
    return lo

def char_positions(t):
    pos = {}
    for idx, c in enumerate(t):
        if c in pos:
            pos[c].append(idx)
        else:
            pos[c] = [idx]
    return pos

def find_next_pos(pattern, pos, i):
    smallest = float("inf")
    for idx, c in enumerate(pattern):
        if c in pos:
            x = bisect_left(pos[c], i + idx)
            if x < len(pos[c]):
                smallest = min(smallest, pos[c][x] - idx)
    return smallest

def min_hamming(text, pattern):
    res = []
    best = len(pattern)
    pos = char_positions(text)

    i = find_next_pos(pattern, pos, 0)
    while i < len(text):
        dist = 0
        for c in range(len(pattern)):
            if i + c >= len(text):
                dist = float("inf")
                break
            if text[i+c] != pattern[c]:
                dist += 1
            c += 1
        if dist != float("inf"):
            res.append((i, dist))
        best = min(best, dist)
        i = find_next_pos(pattern, pos, i + 1)
    return res

s = list(sys.stdin.readline())
distances_yandex = min_hamming(s, "Yandex")
distances_cup = min_hamming(s, "Cup")
distances_yandex.sort(key=lambda x: x[1])
distances_cup.sort(key=lambda x: x[1])
if len(distances_cup) == 0 and len(distances_yandex) == 0:
    result = list("YandexCup") + s[9:]
    print(''.join(result))
elif len(distances_yandex) == 0:
    cup_index = -1
    for i in range(len(distances_cup)):
        if distances_cup[i][0] >= 6:
            cup_index = distances_cup[i][0]
            break
    if cup_index == -1:
        result = list("YandexCup") + s[9:]
        print(''.join(result))
    else:
        result = list("Yandex") + s[6:]
        result[cup_index] = "C"
        result[cup_index + 1] = "u"
        result[cup_inde + 2] = "p"
        print(''.join(result))
elif len(distances_cup) == 0:
    yandex_index = -1
    for i in range(len(distances_yandex)):
        if distances_yandex[i][0] + 6 < len(s) - 3:
            yandex_index = distances_yandex[i][0]
            break
    if yandex_index == -1:
        result = list("YandexCup") + s[9:]
        print(''.join(result))
    else:
        result = s[0:yandex_index] + list("YandexCup") + s[yandex_index + 9:]
        print(''.join(result))
else:
    diff_value = 9
    start_yandex = 0
    start_cup = 6
    for i in range(len(distances_yandex)):
        for j in range(len(distances_cup)):
            if distances_yandex[i][0] + 6 <= distances_cup[j][0]:
                if distances_yandex[i][1] + distances_cup[j][1] < diff_value:
                    start_yandex = distances_yandex[i][0]
                    start_cup = distances_cup[j][0]
                    diff_value = distances_yandex[i][1] + distances_cup[j][1]
    result = s[:start_yandex] + list("Yandex") + s[start_yandex+6:start_cup] + list("Cup") + s[start_cup+3:]
    print(''.join(result))