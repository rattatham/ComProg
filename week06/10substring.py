Text=input("Text: ")
Substring=input("Substring: ")
Text=Text.split()
Textcp=Text.copy()
changer=''
prop=''
asd=[]
#print(Textcp)
for i in range(len(Textcp)):
  if Substring in Text[i]:
    #print(Text[i])
    change=Text[i].split()
    change=[a for a in Text[i]]
    Subs=[a for a in Substring]
    #print(change)
    asd=[]
    #for i in range(len(change)):
    for j in range(len(Subs)):
      if Subs[j] in change:
        asd.append(Subs[j])
    #print(asd)
#print(asd)
for i in range(len(asd)):
  prop=prop+asd[i]
#print(prop)
asd.insert(0,'[')
asd.insert(len(asd),']')
for i in range(len(asd)):
  changer=changer+asd[i]
#print(changer)
#print(len(asd))
if len(asd)==2:
  print("Not found")
else:
  for i in range(len(Textcp)):
    Textcp[i]=str(Textcp[i])
    print(Text[i].replace(prop,changer),end=" ") 
