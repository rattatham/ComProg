n=999999999999999999999999999999999
A=9999999999999999999999999
count=1
max=1
while n!=0:
  n=int(input(""))
  if n==A:
    count+=1
    #print(f"count is {count}")
    if count>max:
      max=count
      show=n
      #print(f"max is {max}")
      #print(f"show is {show}")
  else:
    count=1
    if A==9999999999999999999999999:
      show=n
  A=n
print(max)
print(show)
#print(f"max is {max}")
#print(f"the most consec number is {show}")