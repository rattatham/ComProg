class MyMath:
  def __init__(self):
    sum=3
    for i in range(50):
      sum+=(-1)**i*4/((2+2*i)*(3+2*i)*(4+2*i)) 
    self.pi=sum
    
  def is_even(self,num):
    if num%2==0:
      return True
    else:
      return False

  def fac(self,num):
    if num>20:
      return "factorial TOO LONG."
    else:
      sum=1
      for i in range(1,num+1):
        sum*=i
      return sum

  def divide_by(self,num,k):
    if num%k==0:
      return True
    else:
      return False

  def is_prime(self,num):
    res = True
    for i in range(2,num//2+1):
      if num%i==0:
        res= False
        break
    return res
  def ten_to_bi(self,num):
    x=num
    bi=[]
    binary=''
    while x!=0:
      remainder=x%2
      x=x//2
      bi.append(remainder)
    bi.reverse()
    for i in range(len(bi)):
      bi[i]=str(bi[i])
      binary+=bi[i]
    return binary

  def ten_to_oct(self,num):
    x=num
    oct=[]
    octal=''
    while x!=0:
      remainder=x%8
      x=x//8
      oct.append(remainder)
    oct.reverse()
    for i in range(len(oct)):
      oct[i]=str(oct[i])
      octal+=oct[i]
    return octal

  def ten_to_sixteen(self,num):
    x=num
    hdc=[]
    hexadeci=''
    while x!=0:
      remainder=x%16
      x=x//16
      remainder=self.changeremain(remainder)
      hdc.append(remainder)
    hdc.reverse()
    for i in range(len(hdc)):
      hdc[i]=str(hdc[i])
      hexadeci=hexadeci+hdc[i]
    return hexadeci
  def int_to_roman(self,num):
    ans=''
    x=num
    hundred=x//100
    ten=(x-hundred*100)//10
    one=(x-hundred*100-ten*10)
    ans=self.romanhun(hundred)+self.romanten(ten)+self.romanone(one)
    return ans
  def romanhun(self,hundred):
    res=''
    if hundred==9:
      res+='CM'
      # print(1)
    elif hundred>5:
      x=hundred-5   
      res+='D'+'C'*x
      # print(2)
    elif hundred==5:
      res+='D'
      # print(3)
    elif hundred==4:
      res+='CD'
    elif hundred>0:
      x=hundred
      res+="C"*x
      # print(4)
    return res

  def romanten(self,ten):
    res=''
    if ten==9:
      res+='XC'
    elif ten>5:
      x=ten-5
      res+='L'+'X'*x
    elif ten==5:
      res+='L'
    elif ten==4:
      res+='LX'
    elif ten>0:
      x=ten
      res+="X"*x
    return res

  def romanone(self,one):
    res=''
    if one==9:
      res+="IX"
    elif one>5:
      x=one-5
      res+='V'+'I'*x
    elif one==5:
      res+='V'
    elif one==4:
      res+="IV"
    elif one>0:
      x=one
      res+="I"*x
    return res

  def changeremain(self,n):
    if n==10:
      n='A'
    elif n==11:
      n='B'
    elif n==12:
      n='C'
    elif n==13:
      n='D'
    elif n==14:
      n='E'
    elif n==15:
      n='F'
    elif n==16:
      n='G'
    elif n==17:
      n='H'
    elif n==18:
      n='I'
    elif n==19:
      n='J'
    elif n==20:
      n='K'
    elif n==21:
      n='L'
    elif n==22:
      n='M'
    elif n==23:
      n='N'
    elif n==24:
      n='O'
    elif n==25:
      n='P'
    elif n==26:
      n='Q'
    elif n==27:
      n='R' 
    elif n==28:
      n='S'
    elif n==29:
      n='T'
    else:
      return int(n)
    return n