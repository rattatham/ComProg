def mul_const(A,c):
  ans=zeromat(A)
  for i in range(len(A)):
    for j in range(len(A[i])):
      x=A[i][j]*c
      ans[i][j]=x
  return ans


def zeromat(n):
  sum=[]
  for i in range(len(n)):
    row=[]
    for j in range(len(n[i])):
      row.append(0)
    sum.append(row)   
  return sum


def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      print(f"{A[i][j]:^6}",end=" ")
    print()

A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
c = 2

print_matrix(mul_const(A,c))