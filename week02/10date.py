d=int(input("d: "))
m=int(input("m: "))
y=int(input("y: "))  
days=0
if m>=2:
  for i in range(1,m):  
    if i in [1,3,5,7,8,10,12]:
      days +=31
    elif i==2:
      if (y%4==0 and y%100!=0) or y%400==0:
        days+=29
      else:
        days+=28
    else:
      days+=30
  days+=d
else:
  days+=d
print(days)