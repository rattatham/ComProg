def input_matrix():
    data = []
    for i in range(3):
        data.append([int(j) for j in input(f"Row {i+1} : ").split(' ')])
    return data

class Matrix:
  def __init__(self,matrix:list):
    self.data=matrix
  def det(self):
    mat=self.data
    ans=0
    ans=mat[0][0]*mat[1][1]*mat[2][2]+mat[0][1]*mat[1][2]*mat[2][0]+mat[0][2]*mat[1][0]*mat[2][1]-mat[2][0]*mat[1][1]*mat[0][2]-mat[2][1]*mat[1][2]*mat[0][0]-mat[2][2]*mat[1][0]*mat[0][1]
    return ans
  def plus(self,another):
    ans=[]
    matA=self.data
    matB=another.data
    for i in range(len(matA)):
      row=[]
      for j in range(len(matB)):
        row.append(matA[i][j]+matB[i][j])
      ans.append(row)
    sumplus=Matrix(ans)
    return sumplus
  def minus(self,another):
    ans=[]
    matA=self.data
    matB=another.data
    for i in range(len(matA)):
      row=[]
      for j in range(len(matB)):
        row.append(matA[i][j]-matB[i][j])
      ans.append(row)
    summin=Matrix(ans)
    return summin

  def show(self):      
    for i in range(len(self.data)):
      for j in range(len(self.data)) :
         print(f'{self.data[i][j]:^6}',end=' ')
      print()

  def multiply(self,another):
    A=self.data
    B=another.data
    ans=[]
    for i in range(len(A)):
      row=[]
      for j in range(len(B[0])):
        sum=0
        for k in range(len(A[0])):
          sum+=(A[i][k]*B[k][j])
        row.append(sum)
      ans.append(row)
    summul=Matrix(ans)
    return summul