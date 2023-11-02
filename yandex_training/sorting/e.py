import sys

def print_bucket(b):
    for i in range(len(b)):
        message = ', '.join(b[i]) if len(b[i]) > 0 else "empty"
        print(f"Bucket {i}:", message)

def solution(a):
    curr_list = [i for i in a]
    phase_num = 1
    for i in range(len(a[0]) - 1, -1, -1):
        buckets = [[] for _ in range(10)]
        for j in range(len(curr_list)):
            buckets[int(curr_list[j][i])].append(curr_list[j])
        print("**********")
        print(f"Phase {phase_num}")
        print_bucket(buckets)
        curr_list = []
        for i in range(len(buckets)):
            for j in buckets[i]:
                curr_list.append(j)
        phase_num += 1
    return curr_list
        


n = int(sys.stdin.readline().split()[0])
a = []
for i in range(n):
    a.append(sys.stdin.readline().split()[0])
print("Initial array:")
print(', '.join(a))
result = solution(a)
print("**********")
print("Sorted array:")
print(', '.join(result))