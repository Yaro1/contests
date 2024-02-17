for tc in range (int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    lst=[a[i]+i+1 for i in range (n)]
    lst.sort(reverse=True)
    cur=lst[0]
    for i in range (n):
        if lst[i]<cur:
            cur=lst[i]
        print(cur,end=' ')
        cur-=1          
    print('')
