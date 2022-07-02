def river(l):
  x=str(l)
  l=int(l)
  for i in range(len(x)):
    a=int(x[i])
    l+=a
  return int(l)

river1=1
river2=2
river3=3
a=0
b=0
c=0

n=int(input("N: "))
for i in range(2):
  x=river(n)
  n=x


while True:
  while river1<x:
    a=river(river1)
    river1=a
  if a==x:
    print(1,x)
    break

  while river2<x:
    b=river(river2)
    river2=b
  if b==x:
    print(2,x)
    break

  while river3<x:
    c=river(river3)
    river3=c
  if c==x:
    print(3,x)
    break

  x=river(n)
  n=x