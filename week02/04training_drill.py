dis = int(input("Distance from starting point(m.): "))
mv=0
i=0
while mv != dis:
  if mv<dis:
    mv +=5
    print(mv,end=' ')
    mv -=2
    print(mv,end=' ')
    i+=1
  elif mv>dis:
    mv -=4
    print(mv,end=' ')
    mv +=3
    print(mv,end=' ')
    i+=1
if dis==0:
  print(mv, end=" ")
print(f"\nBuzz moved {i} set(s)")