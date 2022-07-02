def draw(m):
  for i in range(len(m)):
    for j in range(i+1):
      print(m[i],end="")
    print()
number=[]

while number!=['0']:
  draw(number)
  number=input("").split()
else:
  print("Good Bye.")
