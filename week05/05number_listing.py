def chartoint(a):
  for i in range(len(a)):
    a[i]=int(a[i])

def mintomax(a):
  for i in range(len(a)):
    for j in range(len(a)):
      if a[i]<a[j]:
        tmp=a[i]
        a[i]=a[j]
        a[j]=tmp

def cut(a):
  for i in range(len(a)):
    if a[i] not in p:
      p.append(a[i])

num=input("").split()
p=[]
chartoint(num)
mintomax(num)
cut(num)
for i in range(len(p)):
  print(p[i],end=" ")