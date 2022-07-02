Day=int(input("Day: "))
aftr=1
bfr=0
for s in range(1,Day+1):
  fbn=bfr+aftr
  print(fbn,end=" ")
  aftr=bfr
  bfr=fbn

