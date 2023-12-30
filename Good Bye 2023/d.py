
dp=[["1"],["169","196","961"]]

for i in range(5,100,2):
    s="1"+"0"*((i-3)//2)+"6"+"0"*((i-3)//2)+"9"
    temp=[j+"00" for j in dp[-1]]+[s,s[::-1]]
    dp.append(temp)

for _ in range(int(input())):
    n=int(input())
    # print(*dp[n//2])
    for i in dp[n//2]:
        print(i)