#s='WeAreTheChampion'
s=input("Input sentence: ")
#row=4
row=int(input("Input row: "))
a=[i for i in s]
ans=[]
n=0
m=row-2 #row-2
for i in range(row):
  ans.append([])

for i in range(len(a)):
  #print(a[i])
  #print(n,m)
  if n<row:
    ans[n].append(a[i])
    n+=1
  elif n==row:
    if m!=0:
      ans[m].append(a[i])
      m-=1
    else:
      n=0
      ans[n].append(a[i])
      n=1
      m=row-2
  
  #print(ans)
  #input("")
      
for i in range(len(ans)):
  for j in range(len(ans[i])):
    print(ans[i][j],end='')
