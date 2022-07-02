g=input("Grid Size: ").split(" ")
#print(g)
n=int(input("Number of mine(s): "))
b=[]
for i in range(n):
  b.append([])
  x, y=input(f"Mine#{i+1}: ").split()
  b[i].append(x)
  b[i].append(y)
#print(b)
for i in range(len(g)):
  g[i]=int(g[i])
m=[]
for i in range(g[1]):
  row=[]
  for i in range(g[0]):
    row.append(0)
  m.append(row)
#print(m)
for i in range(len(b)):
  x=int(b[i][0])
  y=int(b[i][1])
  m[y][x]="X"
for i in range(len(m)):
  for j in range(len(m[i])):
    if m[i][j]==0:
      sum=0
      if j-1>=0 and m[i][j-1]=='X':
        sum+=1
      if j+1<len(m[i]) and m[i][j+1]=='X':
        sum+=1
      if i-1>=0 and j-1>=0 and m[i-1][j-1]=='X':
        sum+=1
      if i-1>=0 and j>=0 and m[i-1][j]=='X':
        sum+=1
      if i-1>=0 and j+1<len(m[i-1]) and m[i-1][j+1]=='X':
        sum+=1
      if i+1<len(m) and j-1>=0 and m[i+1][j-1]=='X':
        sum+=1
      if i+1<len(m) and j>=0 and m[i+1][j]=='X':
        sum+=1
      if i+1<len(m) and j+1<len(m[i+1]) and m[i+1][j+1]=='X':
        sum+=1
      m[i][j]=sum
for i in range(len(m)):
  for j in range(len(m[i])):
    print(m[i][j],end=" ")
  print()