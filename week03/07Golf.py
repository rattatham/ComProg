total=0
par=input("").split(" ")
shot=input("").split(" ")
#print(par)
#print(shot)
for x in range(0,len(par)):
  a=par[x]
  q=int(a)
  if shot[x]=='Ea':
    total+=q-2
  elif shot[x]=='Bi':
    total+=q-1
  elif shot[x]=='Pa':
    total+=q
  elif shot[x]=='Bo':
    total+=q+1
  elif shot[x]=='DB':
    total+=q+2
print(total)