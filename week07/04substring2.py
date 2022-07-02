def subString(s, ss):
  if len(s) < len(ss):
    return s
  if s[:len(ss)] == ss:
    return '[' + ss + ']' + subString(s[len(ss):], ss)
  if ss in s:
    return s[0] + subString(s[1:], ss)
  if s[:len(ss)] != ss:
    #print(s[:len(ss)] ,ss)
    fss=''
    miss=0
    n=0
    for i in range(len(ss)):
      if s[i]!=ss[i]:
        miss+=1
    if miss<=1:
      x=[x for x in s]
      y=[y for y in ss]
      for i in range(len(ss)):
        if x[i]!=y[i]:
          y[i]='?'
        fss=fss+y[i]
      return '['+fss+']' + subString(s[len(ss):], ss)
    return s[0] + subString(s[1:], ss)


Text=input("Text: ")
Substring=input("Substring: ")
#Text= "acababababaccbabab"
#Substring= "abc"

print(subString(Text,Substring))