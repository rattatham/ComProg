def zeromat(n):
  sum=[]
  for i in range(len(n)):
    row=[]
    for j in range(len(n[i])):
      row.append(0)
    sum.append(row)
  return sum

def createtranspose_matrix(a):
  x=len(a)
  y=len(a[0])
  ans=[]
  for i in range(y):
    row=[]
    for j in range(x):
      row.append(0)
    ans.append(row)
  return ans

def transpose_matrix(A):
  zerotrans=createtranspose_matrix(A)
  for i in range(len(A)):
    for j in range(len(A[i])):
      zerotrans[j][i]=A[i][j]
  return zerotrans

def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      print(f"{A[i][j]:^6}",end=" ")
    print()

A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
c = 2

asd=transpose_matrix(A)
print_matrix(asd)