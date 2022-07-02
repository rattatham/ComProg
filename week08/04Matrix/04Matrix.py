def readfile(fn):
  f=open(fn,"r")
  s=f.read()
  return s

def readMat(s):
  lines = [i.strip() for i in s.split('\n') if i.strip() != '']  
  mat, op, tmp = [], [], []
  for i in lines:
    if i in ['*', '+', '-']:
      mat.append(tmp)
      tmp = []
      op.append(i)
    else:
      tmp.append([int(k) for k in i.split()])
  if len(tmp) > 0:
    mat.append(tmp)
  return mat, op 

def createZeroMat(m, n):
  return [[0 for j in range(n)] for i in range(m)]

def addMat(a, b, op='+'):
  res = createZeroMat(len(a), len(a[0]))
  for i in range(len(a)):
    for j in range(len(a[0])):
      if op == '+':
        res[i][j] = a[i][j] + b[i][j]
      elif op == '-':
        res[i][j] = a[i][j] - b[i][j]
  return res

def mulMat(a, b):
  res = createZeroMat(len(a), len(b[0]))
  for i in range(len(a)):
    for j in range(len(b[0])):
      tmp = 0
      for k in range(len(a[0])):
        tmp += a[i][k] * b[k][j]
      res[i][j] = tmp
  return res 

def processMat(a, b, op):
  if op == '*':
    return mulMat(a, b)
  if op == '+':
    return addMat(a,b)
  if op == '-':
    return addMat(a, b, '-')

def myMatResult(mat, op):
  for i in range(len(op)):
    if i == 0:
      res = processMat(mat[i], mat[i+1], op[i])
    else:
      res = processMat(res, mat[i+1], op[i])
  return res

def printMat(res):
  for i in range(len(res)):
    for j in range(len(res[0])):
        print(f"{res[i][j]:^5}",end=" ")
    print()

fn = input('File name: ')
s=readfile(fn)
mat, op = readMat(s)
res = myMatResult(mat, op)
printMat(res)