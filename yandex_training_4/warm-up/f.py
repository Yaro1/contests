import sys
import sys

def solution():
    answer = 0
    k = int(sys.stdin.readline().split()[0])
    n = int(sys.stdin.readline().split()[0])
    a = []
    for i in range(n):
        a.append(int(sys.stdin.readline().split()[0]))
    b = []
    for i in range(len(a)):
        if a[i] > 0:
            b.append([a[i], i+1])
    # print(answer, b)
    for i in range(len(b) - 1, 0, -1):
        answer += (b[i][0] // k) * b[i][1] * 2
        if b[i][0] % k != 0:
            b[i - 1][0] += (b[i][0] % k)
            answer += 2 * (b[i][1] - b[i - 1][1])
        b[i][0] = 0
    # print(answer, b)
    answer += (b[0][0] // k) * 2 * b[0][1]
    if b[0][0] % k != 0:
        answer += 2 * b[0][1]
    print(answer)

solution()