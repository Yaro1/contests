for _ in range(int(input())):
  s1 = input().strip()
  s2 = input().strip()
  if s1[0] == s2[0]:
    print(f'YES\n{s1[0]}*')
  elif s1[-1] == s2[-1]:
    print(f'YES\n*{s1[-1]}')
  else:
    ks = [k for k in range(len(s1)-1) if s1[k:k+2] in s2]
    if ks:
      s = s1[ks[0]:ks[0]+2]
      print(f'YES\n*{s}*')
    else:
      print('NO')
