def zeromat(A,B):
  sum=[]
  for i in range(len(A)):
    row=[]
    for j in range(len(B[0])):
      row.append(0)
    sum.append(row)
  return sum


def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      print(f"{A[i][j]:^6}",end=" ")
    print()


def mul_matrix(A,B):
  ans=zeromat(A,B)
  for i in range(len(A)):
    for j in range(len(B[0])):
      for k in range(len(B)):
        ans[i][j]+=A[i][k]*B[k][j]
  return ans


A = [[1,2,3],[4,5,6],[7,8,9]]  
B = [[22,13,23],[54,43,21],[23,78,71]]
abc=mul_matrix(A,B)
print_matrix(abc)
