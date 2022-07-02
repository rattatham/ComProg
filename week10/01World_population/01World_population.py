import json

def jsonloads(fn):
  with open(fn) as f:
    s=f.read()
    s=json.loads(s)
  return s

def two(py):
  population=0
  for country in py:
    population+=int(country['population'])
  return population

def three(py):
  frontC=0
  morethanfive=0
  for country in py:
    countryname=country['country']
    if countryname[0]=='C':
      frontC+=1
    if len(countryname)>5:
      morethanfive+=1
  print(frontC)
  print(morethanfive)

def four(py):
  countbil=0
  countbet=0
  count=0
  for country in py:
    if int(country['population'])>500000000:
      countbil+=1
    if 250000000<int(country['population'])<750000000:
      countbet+=1
    if int(country['population'])<10000000:
      count+=1
  print(countbil)
  print(countbet)
  print(count)

def five(py):
  top20pop=0
  middlepop=0
  for i in range(20):
    top20pop+=float(py[i]['World'])
  for i in range(49,150):
    #print(i)
    middlepop+=float(py[i]['World'])
  ans1=top20pop*100
  ans2=middlepop*100
  return f'{ans1:.2f}' , f'{ans2:.2f}'
  print(f'{ans1:.2f}')
  print(f'{ans2:.2f}')

#fn='/tmp/worldpopulation.json'
fn=input('File Name: ')
py=jsonloads(fn)
n=int(input('Input : '))
if n==1:
  print(len(py))
elif n==2:
  print(two(py))
elif n==3:
  three(py)
elif n==4:
  four(py)
elif n==5:
  x,y=five(py)
  print(x)
  print(y)