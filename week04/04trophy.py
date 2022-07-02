n=int(input("n: "))
top=n
sharp=2*n+1
lower=top//2
equal=top*2+3
spacetop=0
spacedown=n+1
equaldown=1
sharpdown=1
for i in range(top):
  for m in range(spacetop):
    print("",end=" ")
  for j in range(equal):
    print("=",end="")
  print("\n",end="")
  for m in range(spacetop):
    print("",end=" ")
  for k in range(1):
    print("=",end="")
    for l in range(sharp):
      print("#",end="")
    print("=",end="")
  print("\n",end="")
  sharp-=2
  equal-=2
  spacetop+=1
for i in range(lower):
  for j in range(spacedown):
    print("",end=" ")
  for k in range(equaldown):
    print("=",end="")
  print("\n",end="")
  for j in range(spacedown-1):
    print("",end=" ")
  for l in range(1):
    print("=",end="")
    for m in range(sharpdown):
      print("#",end="")
    print("=",end="")
  print("\n",end="")
  equaldown+=2
  sharpdown+=2
  spacedown-=1