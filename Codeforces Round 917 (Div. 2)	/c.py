T=int(input())
for _ in range(T):
    n,k,d = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxScore=0
    for i in range(min(2*n+1,d)):
        score = (d-i-1)//2
        for j in range(n):
            if A[j]==j+1:
                score+=1
        for h in range(B[i%k]):
            A[h]+=1
        maxScore=max(maxScore, score)
    print(maxScore)