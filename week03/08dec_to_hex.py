def changeHex(x):
  if x>0:
    hex=''
    while x>0:
      remainder=str(x%16)
      x=x//16
      if remainder=='10':
        hex+='A'
      elif remainder=='11':
        hex+='B'
      elif remainder=='12':
        hex+='C'
      elif remainder=='13':
        hex+='D'
      elif remainder=='14':
        hex+='E'
      elif remainder=='15':
        hex+='F'
      else:
        hex+=remainder
      #print(x,remainder)
    print("Hex: ",end='')
    print(hex[::-1])


while True:
  deci = int(input("Input Decimal: "))
  if deci>0:
    changeHex(deci)
  elif deci==-1:
    print("Good bye.")
    break