import sys
import heapq
 
n, m = sys.stdin.readline().split()
c = [int(i) for i in sys.stdin.readline().split()]
n, m = int(n), int(m)

c_positions = [(i, c[i]) for i in range(len(c))]
c_positions.sort(key=lambda x: (x[1], x[0]))
choosen = [c_positions[0]]
for i in range(1, len(c_positions)):
    if len(choosen) >= m and c_positions[i][1] != choosen[-1][1]:
        break
    choosen.append(c_positions[i])
if len(choosen) > m:
    max_value = max(choosen, key=lambda x: x[1])[1]
    got_items, may_get_items = [], []
    for i in range(len(choosen)):
        if choosen[i][1] != max_value:
            got_items.append(choosen[i])
        else:
            may_get_items.append(choosen[i])
    if got_items:
        leftmost = min(got_items, key=lambda x: x[0])[0]
        righmost = max(got_items, key=lambda x: x[0])[0]
    else:
        leftmost = righmost = None
    cnt_to_get = m - len(got_items)
    result = float("inf")
    r = cnt_to_get - 1
    l = 0
    while r < len(may_get_items):
        if (leftmost is not None) and (righmost is not None):
            result = min(result, max(righmost, may_get_items[r][0]) - min(leftmost, may_get_items[l][0]) + 1)
        else:
            result = min(result, may_get_items[r][0] - may_get_items[l][0] + 1)
        r += 1
        l += 1
    print(result)
else:
    leftmost, rightmost = float("inf"), float("-inf")
    for i in range(len(choosen)):
        leftmost = min(leftmost, choosen[i][0])
        rightmost = max(rightmost, choosen[i][0])
    print(rightmost - leftmost + 1)