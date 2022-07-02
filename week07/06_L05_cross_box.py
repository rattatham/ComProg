def rectrangle(n):
  a=[]
  for i in range(n):
    row=[]
    for j in range(n):
      row.append(' ')
    a.append(row)
#print(a)
  for i in range(n):
    if i ==0:
      for k in range(n):
        a[i][k]='.'
    elif i==n-1:
      for k in range(n):
        a[i][k]='.'
    elif i==n//2:
      a[i][0]='.'
      a[i][-1]='.'
      a[i][i]='.'
    else:
      a[i][0]='.'
      a[i][-1]='.'
      a[i][i]='.'
      a[i][-i-1]='.'
  return a
def printrec(a):
  for i in range(len(a)):
    for j in range(len(a)):
      print(a[i][j],end='')
    print()
#print(a)
n=int(input(""))
a=rectrangle(n)
printrec(a)