import sys


# max count sets = 2x - 1
# max count ros = 2y - 1
# min count sets = x
# min count ros = y

# x*y <= number_of_games <= (2x-1)*(2y-1)
# y <= number_of_games <= 2y - 1

# count_a count_b
# max(count_a, count_b) == x*y
# 0 <= min(count_a, count_b) < x*y


def task(t):
    for _ in range(t):
        n = int(sys.stdin.readline().split()[0])
        winner_results = [[] for _ in range(n)]
        winner = list(sys.stdin.readline().split()[0])
        for i in range(1, n+1):
            k = 0
            curr_res = [0, 0]
            while k < n:
                if winner[k] == "A":
                    curr_res[0] += 1
                else:
                    curr_res[1] += 1
                if curr_res[0] == i or curr_res[1] == i:
                    winner_results[i - 1].append(curr_res[0] > curr_res[1])
                    curr_res = [0, 0]
                k += 1
            if curr_res != [0, 0]:
                winner_results[i - 1] = ["?"]
        # print(winner_results)
        valid_results = set()
        for res in winner_results:
            a = sum(1 for i in res if i == True)
            b = sum(1 for i in res if i == False)
            if (a > b and res[-1] == True):
                # print("Winner A", res)
                valid_results.add("A")
            elif (a < b and res[-1] == False):
                # print("Winner B", res)
                valid_results.add("B")
        if len(valid_results) == 0 or len(valid_results) == 2:
            print("?")
        else:
            print(valid_results.pop())


        


t = int(sys.stdin.readline().split()[0])
task(t)