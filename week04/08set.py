A=input("Input setA: ").split()
B=input("Input setB: ").split()
intersect=[]
AminB=A.copy()
BminA=B.copy()
AuB=[]
empt=[]
for i in range(len(A)):
  for j in range(len(B)):
    if A[i]==B[j]:
      x=A[i]
      intersect.append(x)

for i in range(len(A)):
  for j in range(len(B)):
    if A[i]==B[j]:
      AminB.remove(A[i])
      

for i in range(len(A)):
  for j in range(len(B)):
    if A[i]==B[j]:
      BminA.remove(B[j])

for i in range(len(A)):
  if A[i] not in AuB:
    AuB.append(A[i])
for i in range(len(B)):
  if B[i] not in AuB:
    AuB.append(B[i])

if intersect==[]:
  print("A intersect B: empty set",end="")
else:
  print("A intersect B: ",end="")
  for i in range(len(intersect)):
    print(intersect[i],end=" ")
print("\n",end="")
if AminB==empt:
  print("A minus B: empty set",end="")
else:
  print("A minus B: ",end="")
  for i in range(len(AminB)):
    print(AminB[i],end=" ")
print("\n",end="")
if BminA==empt:
  print("B minus A: empty set",end="")
else:
  print("B minus A: ",end="")
  for i in range(len(BminA)):
    print(BminA[i],end=" ")
print("\n",end="")
if AuB==[]:
  print("empty set",end="")
else:
  print("A union B: ",end="")
  for i in range(len(AuB)):
    AuB[i]=int(AuB[i])
  AuB.sort()
  for i in range(len(AuB)):
    print(AuB[i],end=" ")