text=input("Text: ")
text=text.split(" ")
chain=0
length=0
miss=0
n=0
lengthmax=-999999999
while n+1<len(text):
 
  x=[]
  y=[]
  x=[x for x in text[n]]
  y=[y for y in text[n+1]]
  #print(text[n],text[n+1])
  for i in range(len(x)):
    if x[i]!=y[i]:
      #print(x[i],y[i])
      miss+=1
  if miss>2:
    #print(x,y)
    chain+=1
    length=0
  elif miss<=2:
    length+=1
    #print(length)
    if length>lengthmax:
      lengthmax=length
  miss=0
  n+=1
else:
  print(f"{chain+1} Chain(s). Maximum length is {lengthmax+1} word(s).")