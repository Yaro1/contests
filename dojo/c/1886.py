for _ in range(int(input())):
    s=input()
    p=int(input())
    n=len(s)
    k=0
    while p>n-k:
        p-=n-k
        k+=1
    l=[]
    for i in s:
        while k and l and l[-1]>i :
            l.pop()
            k-=1
        l.append(i)
    print(l[p-1],end='')