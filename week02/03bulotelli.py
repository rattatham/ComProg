inj = input("Is Bulotelli injured?(y/n) ")
if inj == 'y':
  print("Not available")
elif inj == 'n':
  late = input("Is Bulotelli late for the training?(y/n) ")
  if late =='n':
    print("Starter")
  elif late =='y':
    perf = input("Did Bulotelli perform well in training?(y/n) ")
    if perf =='y':
      print("Substitute")
    elif perf == "n":
      print("Not selected")
