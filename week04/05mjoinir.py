def mjonir():
  for i in range(space):
    print("",end=(" "))
  for i in range(edge):
    print("o",end="")
  print("\n",end="")
  for i in range(topcore):
    for i in range(top):
      print("o",end="")
    print("\n",end="")
  for i in range(space):
    print("",end=(" "))
  for i in range(edge):
    print("o",end="")
  print("\n",end="")
  for i in range(griplong):
    for k in range(spacelower):
      print("",end=" ")
    for j in range(gripcore):
      print("o",end="")
    print("\n",end="")
  for i in range(lowgripline):
    for i in range(spacelowgrip):
      print("",end=" ")
    for i in range(lowgrip):
      print("o",end="")
    print("\n",end="")
  for i in range(spacelower):
    print("",end=" ")
  for i in range(lowest):
    print("o",end="")

def level(a):
  n=a//1000
  return n
edge=7
top=9
topcore=3
griplong=3
gripcore=1
lowgrip=3
space=1
spacelower=4
lowest=1
spacelowgrip=3
lowgripline=1

gold=float(input("Input Gold: "))
if gold<1000:
  print("Not enough gold.")
else:
  for i in range(int(level(gold))-1):
    edge+=3
    top+=3
    topcore+=2
    griplong+=1
    gripcore+=1
    lowgrip+=1
    spacelower+=1
    lowest+=1
    spacelowgrip+=1
    lowgripline+=1
  mjonir()