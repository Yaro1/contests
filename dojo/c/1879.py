mod = 998244353

for _ in range(int(input())):
   s = input()
   n = len(s)
   k = n
   ans = 1
   i = 0
   while(i<n):
      r = i + 1
      while(r < n and s[r] == s[i]):
         r += 1
      ans = (ans * (r - i)) % mod
      k -= 1
      i = r
   for i in range(1,k+1):
      ans = ans * i % mod
   
   print(k,ans)