x=input("").split()
code=[]
#print(x)
#print(x[0])
skip=int(x[0])
for i in range(1,len(x),skip+1):
  x[i]=int(x[i])
  code.append(x[i])
#print(code)
for j in range(len(code)):
  print(chr(code[j]),end="")
