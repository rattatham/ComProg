n=input("Input: ").split()
a=[]
for i in range(len(n)): 
  for j in range(i+1,len(n)):
    n[i]=int(n[i])
    n[j]=int(n[j])
    x=n[i]+n[j]
    if x not in a:
      if x<=100 and x>=-100:
        a.append(x)
a.sort()
for i in range(len(a)):
  print(a[i],end=" ")