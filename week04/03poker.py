def find(a, n):
  res = -1
  for i in range(len(a)):
    if a[i] == n:
      return i
  return -1

card=input("Cards: ").split()
#print(card)
a=[]
b=[]
for i in range(len(card)):
  if card[i] not in a:
    a.append(card[i])
    b.append(1)
  else:
    n=find(a,card[i])
    b[n]+=1
#print(a,b)
result=max(b)
if result==4:
  print("Mark got \"Four of a kind\"")
elif 3 in b and 2 in b:
  print("Mark got \"Full House\"")
elif result==3:
  print("Mark got \"Three of a kind\"")
else:
  print("Mark got \"High Card\"")