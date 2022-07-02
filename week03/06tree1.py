h=int(input("h: "))
s=input("Character: ")
invert=input("Is the tree invert?(y/n): ")
stalk=h//2
leaf=h*2-1
spacein=0
space=h-1
leaflower=1
if invert=='y':
  for i in range(stalk):
    for j in range(h-1):
      print("",end=" ")
    print(f"{s}",end="")
    print("\n",end="")
  for x in range(h):
    for z in range(spacein):
      print(" ",end="")    
    for y in range(leaf):
      print(s,end="")
    print("\n",end="")
    leaf-=2
    spacein+=1


elif invert=='n':
  for x in range(h):
    for y in range(space,0,-1):
      print(" ",end="")
    for z in range(leaflower):
      print(s,end="")
    print("\n",end="")
    leaflower+=2
    space-=1


  for i in range(stalk):
    for j in range(h-1):
      print("",end=" ")
    print(f"{s}",end="")
    print("\n",end="")
  