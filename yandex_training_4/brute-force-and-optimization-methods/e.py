import sys
from collections import defaultdict

def correct_sequences(n, path, stack, open_1, open_2):
    if len(path) == n:
        print(path)
        return
    empty = (n - len(path) - open_1 - open_2) // 2
    if empty > 0:
        correct_sequences(n, path + "(", stack + ["("], open_1 + 1, open_2)
        correct_sequences(n, path + "[", stack + ["["], open_1, open_2 + 1)
    if stack and stack[-1] == "(":
        correct_sequences(n, path + ")", stack[:len(stack) - 1], open_1 - 1, open_2)
    if stack and stack[-1] == "[":
        correct_sequences(n, path + "]", stack[:len(stack) - 1], open_1, open_2 - 1)
        
            

def solution():
    n = int(sys.stdin.readline().split()[0])
    correct_sequences(n, "", [], 0, 0)
    

solution()