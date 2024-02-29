import sys
 
def solution():
    n = int(sys.stdin.readline().split()[0])
    a1 =  input()
    a2 = input()
    a = [[], []]
    for i in a1:
        a[0].append(i)
    for i in a2:
        a[1].append(i)
    result = [a[0][0]]
    stack = []
    for i in range(n):
        if i == n - 1:
            result.append(a[1][n - 1])
            break
        if a[1][i] < a[0][i + 1]:
            result += [j for j in a[1][i:]]
            break
        elif a[1][i] > a[0][i + 1]:
            result.append(a[0][i + 1])
            stack = []
        else:
            result.append(a[0][i + 1])
            stack.append(i)
    print(''.join(result))
    print(1 + len(stack))
        
    
 
t = int(sys.stdin.readline().split()[0])
for _ in range(t):
    solution()
