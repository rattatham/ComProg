def checkeach(a):
  res=0
  for i in range(len(a)-1):
    if bracket[a[i]]==a[i+1]:
      #print(a[i],a[i+1])
      res+=1
  # print(res)
  # print(len(a)/2)
  x=a[12:]
  y=a[:12]
  if res==len(a)/2:
    #print('checkeach')
    return True
  else:
    if checkskip(x) and checkskip(y):
      return True
    else:
      return checkskip(a)

def checkskip(a):
  res=0
  for i in range(len(a)//2):
    if i==0:
      if bracket[a[i]]==a[len(a)-1]:
        #print(a[i],a[len(a)-1])
        res+=1
    else:
      if bracket[a[i]]==a[-i-1]:
        res+=1
  if res==len(a)/2:
    return True
  else:
    return False

class py_solution:
  def __init__(self,string):
    lis=[i for i in string if i!='.']
    self.lis=lis
  def is_valid_parentheses(self):
    return checkeach(self.lis)

string=input('input: ')
#string='((((([]))))){{{{{[]}}}}}'
bracket={'(':')','[':']','{':'}',')':'(',']':'[','}':'{'}
a=py_solution(string)
#print(a.is_valid_parentheses())
if a.is_valid_parentheses():
  print('valid parentheses')
else:
  print('invalid parentheses')