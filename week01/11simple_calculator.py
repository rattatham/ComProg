x=int(input("x: "))
op=input("Operator: ")
y=int(input("y: "))
if op=="+":
  print(x+y)
else:
  if op=="-":
    print(x-y)
  else:
    if op=="/":
      print(f"{x/y:.2f}")
    else:
      if op=="*":
        print(x*y)
      else:
        if op=="%":
          print(x%y)
        else:
          print("Unknown Operator")