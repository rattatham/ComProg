def findmax(a):
  mymax=-9999999999999
  len_a=len(a)
  for i in range(len_a):
    if a[i]>mymax:
      mymax=a[i]
  return mymax

def findmax2(a):
  mymax=-9999999999999
  len_a=len(a)
  res=-1
  for i in range(len_a):
    if a[i]>mymax:
      mymax=a[i]
      res=i
  return res

def findmin(a):
  mymin=99999999999999999999999
  len_a =len(a)
  res=-1
  for i in range(len_a):
    if a[i]<mymin:
      mymin=a[i]
      res=i
  return mymin

def chartoint(a):
  for i in range(1,len(a)):
    a[i]=int(a[i]) 

sum=0
n=int(input("n = "))
m=int(input("m = "))
s1=[]
s2=[]
for i in range(n):
  nm=input("")
  x=nm.split(" ")
  chartoint(x)
  s1.append(x[0])
  x.pop(0)
  #print(x)
  x.remove(findmin(x))
  for i in range(len(x)):
    sum+=x[i]
  s2.append(sum)
  sum=0

print(findmax(s2))
j=findmax(s2)
for i in range(len(s2)):
  if s2[i]==j:
    print(s1[i])
#print(s1,"\n", s2)