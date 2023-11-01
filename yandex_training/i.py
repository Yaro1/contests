import sys

def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] in "{[(":
            stack.append(s[i])
        elif len(stack) == 0:
            print("no")
            return
        elif s[i] == "}" and stack[-1] == "{":
            stack.pop()
        elif s[i] == "]" and stack[-1] == "[":
            stack.pop()
        elif s[i] == ")" and stack[-1] == "(":
            stack.pop()
        else:
            print("no")
            return
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
    

s = input()
solution(s)