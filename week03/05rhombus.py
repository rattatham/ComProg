L=int(input("input: "))
sharp=1
upper=L//2+1
lower=L-upper
spaceup=L//2
spacedown=1
sharpdown=L-2
for i in range(upper,0,-1):
  for j in range(spaceup):
    print("",end=" ")
  for k in range(sharp):
    print("#",end="")
  print("\n",end='')
  sharp+=2
  spaceup-=1
for x in range(lower):
  for y in range(spacedown):
    print("",end=" ")
  for k in range(sharpdown):
    print('#',end="")
  print("\n",end='')
  sharpdown-=2
  spacedown+=1
