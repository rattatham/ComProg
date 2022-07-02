p=[]
a=9999
while a!=0:
  a=input("Input: ")
  x=0
  for i in range(len(a)):
    n=int(a[i])
    x+=(n)**(i+1)
  a=int(a)
  if x==a:
    p.append("Y")
  else:
    p.append("N")
else:
  for i in range(len(p)-1):
    print(p[i],end="")