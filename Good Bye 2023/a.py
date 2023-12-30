import sys
 
DELIMETERS = [1, 7, 17, 119, 289, 2023]

def solution():
    n, k = map(int, input().split())
    b = [int(i) for i in input().split()]
    curr_item = 2023
    for i in b:
        if curr_item % i != 0:
            print("NO")
            return
        curr_item //= i
    print("YES")
    if curr_item == 1:
        print(*[1 for _ in range(k)])
    elif curr_item == 7:
        print(*([7] + [1 for _ in range(k - 1)]))
    elif curr_item == 17:
        print(*([17] + [1 for _ in range(k - 1)]))
    elif curr_item == 119:
        print(*([119] + [1 for _ in range(k - 1)]))
    elif curr_item == 289:
        print(*([289] + [1 for _ in range(k - 1)]))
    elif curr_item == 2023:
        print(*([2023] + [1 for _ in range(k - 1)]))
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()