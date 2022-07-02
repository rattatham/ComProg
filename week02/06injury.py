et = int(input("Estimated time : "))
week = et//8
pt=0
wt=0
ft=0
apt=0
awt=0
aft=0
for i in range(1,week+1):
  print(f"Week{i}")
  pt = int(input("Physical therapy : "))
  wt = int(input("Weight training : "))
  ft = int(input("Fitness training : "))
  apt+=pt
  awt+=wt
  aft+=ft
if apt>=2.5*et and awt>=2.5*et and aft>=2.5*et:
  print("Buzzy has recovered in time.")
else:
  print("Buzzy has not recovered in time.")