def pure(matlis):
  purelis=list()
  for i in range(len(matlis)-2):
    for j in range(len(matlis)-2):
      sum=0
      for k in range(i,i+3):
        for l in range(j,j+3):
          sum+=int(matlis[k][l])
      purelis.append(sum/9)
  return purelis
def grade(purelis,matlis):
  A=True
  B=True
  for percent in purelis:
    #print(percent)
    if percent<85:
      #print('Not A')
      A=False
    if percent<70:
      #print('Not B')
      B=False
    if percent<60:
      #print('NG')
      return grade1('No Grade',matlis)
  if A:
    return grade1('Grade A',matlis)
  elif B:
    return grade1('Grade B',matlis)
  else:
    return grade1('Grade C',matlis)
  
def grade1(grade,matlis):
  area=len(matlis)*len(matlis[0])
  tmp=0
  if grade=='Grade A':
    return print('Output: Grade A')
  elif grade=='Grade B':
    for i in range(len(matlis)):
      for j in range(len(matlis[i])):
        if matlis[i][j]>=90:
          tmp+=1
    if tmp/area*100>25:
      return print('Output: Grade A (Upgrade From B)')
    else:
      return print('Output: Grade B')
  elif grade=='Grade C':
    for i in range(len(matlis)):
      for j in range(len(matlis[i])):
        if matlis[i][j]>=85:
          tmp+=1
    if tmp/area*100>25:
      return print('Output: Grade B (Upgrade From C)')
    else:
      return print('Output: Grade C')
  elif grade=='No Grade':
    for i in range(len(matlis)):
      for j in range(len(matlis[i])):
        if matlis[i][j]>=70:
          tmp+=1
    if tmp/area*100>25:
      return print('Output: Grade C (Upgrade From No Grade)')
    else:
      return print('Output: No Grade')


size=int(input("Material size: "))
matlis=list()
for i in range(size):
  row=input('')
  tmp=[int(x) for x in row.split()]
  matlis.append(tmp)
#matlis=[[72, 65, 78, 82, 97], [82, 100, 95, 86, 46], [92, 85, 97, 94, 98], [85, 99, 100, 100, 67], [65, 84, 79, 89, 74]]
#print(matlis)
purelis=pure(matlis)
#print(purelis)
grade(purelis,matlis)