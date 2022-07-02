a=[]
i=0
while i!=5:
  n=int(input("Enter a positive number: "))
  if n>0:
    i+=1
    a.append(n)
a.sort()
b=len(a)
me=b//2
sum=0
for i in range(b):
  sum+=a[i]
print(f"sum: {sum}")
print(f"min: {min(a)}")
print(f"max: {max(a)}")
print(f"med: {a[me]}")
