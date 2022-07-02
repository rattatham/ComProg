def anytoten(any,n):
  s=list(any)
  sum=0
  x=len(s)-1
  for i in range(len(s)):
    if s[i]<'99999999999999999999' and s[i]>'-99999999999999999999999':
      s[i]=int(s[i])
    elif s[i]=='A':
      s[i]=10
    elif s[i]=="B":
      s[i]=11
    elif s[i]=='C':
      s[i]=12
    elif s[i]=='D':
      s[i]=13
    elif s[i]=='E':
      s[i]=14
    elif s[i]=='F':
      s[i]=15
  for i in range(len(s)):
    #print(s[i],"         ",x)
    sum+=s[i]*(n**x)
    x-=1
  return sum

def tentoany(ten,m):
  result=''
  while ten>0:
    if ten%m>9:
      if ten%m==10:
        result = 'A' + result
        ten = ten // m
      elif ten%m==11:
        result = 'B' + result
        ten = ten // m
      elif ten%m==12:
        result = 'C' + result
        ten = ten // m
      elif ten%m==13:
        result = 'D' + result
        ten = ten // m
      elif ten%m==14:
        result = 'E' + result
        ten = ten // m
      elif ten%m==15:
        result = 'F' + result
        ten = ten // m
    else:
      result = str(ten%m) + result
      ten=ten//m
  return result

n=int(input(""))
m=int(input(""))
any=input()
sum=anytoten(any,n)
#print(sum)
sum2=tentoany(sum,m)
print(sum2)