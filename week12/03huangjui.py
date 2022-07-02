def inputland():
  land=[]
  n='asdasd'
  while n!='':
    n=input('')
    x=[int(x) for x in n.split()]
    if n!='':
      land.append(x)
  return land

def pay(land):
  for i in range(len(land)):
    if len(land[i])!=len(land[0]):
      return print('Can\'t Buy')
  return minland(land)

def minland(land):
  min=99999999
  for i in range(len(land)-1):
    for j in range(len(land[i])-1):
      tmp=0
      tmp+=land[i][j]+land[i][j+1]*1.1+land[i+1][j+1]*1.1+land[i+1][j]*1.1*1.1
      if tmp<min:
        min=tmp
      tmp=0
      tmp+=land[i+1][j]+land[i+1][j+1]*1.1+land[i][j+1]*1.1+land[i][j]*1.1*1.1
      if tmp<min:
        min=tmp
  return  print(f'{min:.2f}')

land=inputland()
pay(land)
