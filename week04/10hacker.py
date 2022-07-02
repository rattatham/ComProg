pwd=int(input(""))
first=pwd//100
second=(pwd-first*100)//10
last=pwd-first*100-second*10
fdig=int(input(""))
if fdig==first:
  sdig=int(input(""))
  if sdig==second:
    tdig=int(input(""))
    if tdig==last:
      print("Succeed!!")
    else:
     print("Fail!!")
  else:
    print("Fail!!")
else:
  print("Fail!!")
