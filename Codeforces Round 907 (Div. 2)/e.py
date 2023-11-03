import sys
import heapq
import math


def solution():
    n, k = map(int, sys.stdin.readline().strip().split())
    a_list = list(map(int, sys.stdin.readline().split()))

    def coprime(a, b):
        return math.gcd(a, b) == 1

    con_pairs = []
    con_ones = []
    special_con_ones = []

    curr = 0
    prev = 1
    con_one = 0

    divs, rems = 0, 0
    for i, num in enumerate(a_list):
        if con_one:
            if num == 1:
                con_one += 1
                continue
            else:
                con_ones.append(con_one)
                con_one = 0
                prev = num
                continue
        if num == 1:
            con_one = 1
            if curr:
                con_pairs.append(curr)
                curr = 0
            prev = 1
            continue

        if i == 0:
            prev = num
            continue

        if coprime(num, prev):
            curr += 1
        else:
            if curr:
                con_pairs.append(curr)
            curr = 0
        prev = num

    if curr:
        con_pairs.append(curr)

    if con_one:
        rems += con_one
        if all(num == 1 for num in a_list):
            return max(0, con_one - k)

    if a_list[0] == 1:
        rems += con_ones.pop(0)

    con_ones.sort()
    special_con_ones.sort()
            
    ans = 0
    divs += sum(i >> 1 for i in con_pairs)
    rems += sum(i & 1 for i in con_pairs)

    r_divs = min(divs, k)
    divs -= r_divs
    k -= r_divs

    for i in range(len(con_ones)):
        if k >= con_ones[i]:
            k -= con_ones[i]
        else:
            ans += con_ones[i] + 1

                    
    r_rems = min(rems, k)
    rems -= r_rems
    k -= r_rems

    ans = ans + 2 * divs + rems
    if ans and k:
        ans = max(0, ans - k)
    return ans

t = int(sys.stdin.readline())

for _ in range(t):
    print(solution())
