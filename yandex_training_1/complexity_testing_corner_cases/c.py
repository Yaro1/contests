import sys

def processing_number(number):
    replaced = number.replace("-", "").replace("(", "").replace(")", "")
    if replaced[0] == "+":
        return replaced[2:12] if len(replaced) == 12 else None
    elif replaced[0] == "8" and len(replaced) == 11:
        return replaced[1:11] if len(replaced) == 11 else None
    else:
        return "495" + replaced[0:7] if len(replaced) == 7 else None
    

def solution(numbers):
    number_first = processing_number(numbers[0])
    if not number_first:
        print("NO\nNO\nNO")
        return
    for num in range(1, len(numbers)):
        processed = processing_number(numbers[num])
        if processed and processed == number_first:
            print("YES")
        else:
            print("NO")
    
    

numbers = [sys.stdin.readline().split()[0] for i in range(4)]
solution(numbers)