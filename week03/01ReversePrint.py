def check(a):
  if a==0:
    return False
  else:
    return True
l=[]
while True:
  x=int(input(""))
  if check(x):
    l.append(x)
    pass
  else:
    break
l.reverse()
#print(l)
for b in l:
  print(b,end=" ")
