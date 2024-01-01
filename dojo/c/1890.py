from sys import stdin
def input(): return stdin.readline()[:-1]
for _ in range(int(input())):
	n=int(input())
	s=input()
	if n%2:
		print(-1)
		continue
	i=0
	j=n-1
	c=0
	ans=[]
	while i<j and c<300:
		if s[i]==s[j]:
			if s[i]=="0":
				s=s[0:j+1]+"01"+s[j+1:]
				ans.append(j+1)
				i+=1
				j+=1
			else:
				s=s[0:i]+"01"+s[i:]
				ans.append(i)
				i+=1
				j+=1
			c+=1
		else:
			i+=1
			j-=1
	if c==300:
		print(-1)
	else:
		print(len(ans))
		print(*ans)