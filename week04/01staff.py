def Alpha(n):
  n=n.lower()
  if n>='a' and n<='z':
    return True
  else:
    return False

def Number(n):
  if n>='1' and n<='9':
    return True
  else:
    return False
alpha=[]
number=[]
special=[]
a=input("").split()
#print(a)
for i in range(len(a)):
  x=a[i]
  if Alpha(x):
    alpha.append(x)
  elif Number(x):
    number.append(x)
  else:
    special.append(x)
print(f"Alphabet: {alpha}")
print(f"Number: {number}")
print(f"Special: {special}")