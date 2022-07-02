def createzerotrans(A):
  x=len(A)
  y=len(A[0])
  zerotrans=[]
  for i in range(y):
    row=[]
    for j in range(x):
      row.append(0)
    zerotrans.append(row)
  return zerotrans

def transpose_matrix(A):
  transpose=createzerotrans(A)
  for i in range(len(A)):
    for j in range(len(A[i])):
      transpose[j][i]=A[i][j]
  return transpose

def zeromat(A):
  sum=[]
  for i in range(len(A)):
    row=[]
    for j in range(len(A[i])):
      row.append(0)
    sum.append(row)
  return sum

def zeromatmul(A,B):
  sum=[]
  for i in range(len(A)):
    row=[]
    for j in range(len(B[0])):
      row.append(0)
    sum.append(row)
  return sum

def plus_matrix(A,B):
  plusmat=zeromat(A)
  for i in range(len(A)):
    for j in range(len(A[i])):
      plusmat[i][j]=A[i][j]+B[i][j]
  return plusmat

def minus_matrix(A,B):
  minmat=zeromat(A)
  for i in range(len(A)):
    for j in range(len(A[i])):
      minmat[i][j]=A[i][j]-B[i][j]
  return minmat

def mul_matrix(A,B):
  mulmat=zeromatmul(A,B)
  for i in range(len(A)):
    for j in range(len(B[0])):
      for k in range(len(B)):
        mulmat[i][j]+=A[i][k]*B[k][j]
  return mulmat

def power_matrix(A,c):
  if c==1:
    x=A
  elif c==0:
    return [[1,0],[0,1]]
  else:
    x=A
    for i in range(c-1):
      x=mul_matrix(x,A)
  return x

def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      print(f"{A[i][j]:^6}",end=" ")
    print()

A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
D = [[100,50],[20,70]]
c = 2

B=transpose_matrix(B)
ab=plus_matrix(A,B)
C=power_matrix(C,c)
cd=minus_matrix(C,D)
answer=mul_matrix(ab,cd)
print_matrix(answer)
