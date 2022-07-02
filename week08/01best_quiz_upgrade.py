def manage(a):
  a.sort()
  a.pop(0)
  a.pop(len(a)-1)
  return a

def append(a):
  point=[]
  for i in range(len(a)):
    score=[]
    for j in range(len(a[i])):
      if j!=0:
        s[i][j]=int(s[i][j])
        score.append(s[i][j])
      else:
        name.append(s[i][j])
    x=0
    score=manage(score)
    for i in score:
      x+=i
    point.append(x)
  return point,name

def swap(a,b):
  for i in range(len(a)):
    for j in range(len(a)):
      if a[i]>a[j]:
        tmp=a[i]
        a[i]=a[j]
        a[j]=tmp
        tmp=b[i]
        b[i]=b[j]
        b[j]=tmp
  return a,b

def findmax(a,b):
  mymax=-999999
  topn=[]
  tops=[]
  for i in range(len(a)):
    if a[i]>=mymax:
      mymax=a[i]
      tops.append(mymax)
      topn.append(b[i])
  return tops,topn

def read(fname):
#   f=open(f"{fname}","w")
#   f.write('''Non 9 8 7 8 8
# Prince 3 5 4 2 10
# Khanun 7 7 9 9 6
# Plapud 0 9 7 8 10
# Queen 10 7 7 8 7''')
#   f.close()
  f=open(f"{fname}","r")
  s=f.read()
  f.close
  return s


finame=input("File name: ")
s=read(finame)
s=s.split("\n")
for i in range(len(s)):
  s[i]=s[i].split(" ")
name=[]
point=[]
point,name = append(s)
point,name = swap(point,name)
fins,finn = findmax(point,name)
print(fins[0])
for i in finn:
  print(i)