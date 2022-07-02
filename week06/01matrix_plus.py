def plus_matrix(A,B):
  ans=zeromat(A)
  for i in range(len(A)):
    for j in range(len(A[i])):
      x=A[i][j]+B[i][j]
      ans[i].append(x)
  return ans

def zeromat(n):
  sum=[]
  for i in range(len(n)):
    row=[]
    sum.append(row)
  return sum

def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      print(f"{A[i][j]:^6d}",end=" ")
    print()


A = [[1,2,3],[4,5,6],[7,8,9]]  
B = [[22,13,23],[54,43,21],[23,78,71]]

plus_matrix(A,B)
print_matrix(plus_matrix(A,B))