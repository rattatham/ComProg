def plan(R,C):
  square=0
  side=1
  if R<C:
    tmp=R
  else:
    tmp=C
  while side<=tmp:
    square+=R*C
    R-=1
    C-=1
    side+=1
  return square

R=int(input('R: '))
C=int(input('C: '))
print(plan(R,C))