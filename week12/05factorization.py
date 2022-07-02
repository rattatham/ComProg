n=int(input("n: "))
ans=[]
while n!=1:
  for i in range(2,99999):
    if n%i==0:
      n=n/i
      ans.append(i)
      break
for x in ans:
  print(x,end=' ')