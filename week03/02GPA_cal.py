s=int(input("How many subject: "))
def checkgrade(x):
  if x=='A':
    return 4
  elif x=='B+':
    return 3.5
  elif x=='B':
    return 3
  elif x=='C+':
    return 2.5
  elif x=='C':
    return 2
  elif x=='D+':
    return 1.5
  elif x=='D':
    return 1
credit=[]
ncredit=0
grade=[]
sum=0
i=0
while i<s:
  i+=1
  c=int(input(f"Subject {i} Credits: "))
  b=input(f"Subject {i} Grade: ")
  g=checkgrade(b)
  #credit.append(c)
  grade.append(g)
  sum+=g*c
  ncredit+=c
#print(ncredit)
#print(sum)
GPA=sum/ncredit
print(f"Output: Total Credit = {ncredit:.1f} ,GPA = {GPA:.2f}")