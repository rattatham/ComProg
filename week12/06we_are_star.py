def matrix(n):
  mat=[]
  for i in range(n):
    row=[]
    for j in range(n):
      row.append(' ')
    mat.append(row)
  return mat
def printmat(mat):
  for i in range(len(mat)):
    for j in range(len(mat[i])):
      print(mat[i][j],end='')
    print()

def createmat(n):
  mat=matrix(n)
  n=0
  for i in range(len(mat)):
    #print(i,n)
    mat[i][0+n]='+'
    mat[i][-1-n]='+'
    n+=1
  for i in range(len(mat)):
    for j in range(len(mat[i])):
      if j==n//2:
        mat[i][j]='+'
      if i==n//2:
        mat[i][j]='+'
  return printmat(mat)

n=int(input("n: "))
createmat(n)
# mat=matrix(n)

# n=0
# for i in range(len(mat)):
#   #print(i,n)
#   mat[i][0+n]='+'
#   mat[i][-1-n]='+'
#   n+=1
# for i in range(len(mat)):
#   for j in range(len(mat[i])):
#     if j==n//2:
#       mat[i][j]='+'
#     if i==n//2:
#       mat[i][j]='+'

# printmat(mat)
