import sys
import copy

t = int(sys.stdin.readline().split()[0])
l = [0 for _ in range(35)]
for _ in range(t):
    t, value = map(int, input().split())
    if t == 1:
        l[value] += 1
    else:
        checking = [int(i) for i in bin(value)[2:]][::-1]
        check_l = [i for i in l]
        flag = True
        for i in range(min(len(check_l), len(checking))):
            if check_l[i] < checking[i]:
                flag = False
                break
            else:
                if checking[i] == 1:
                    check_l[i+1] += (check_l[i] - 1) // 2
                else:
                    check_l[i+1] += check_l[i] // 2
        if flag:
            print("YES")
        else:
            print("NO")