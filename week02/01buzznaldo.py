min = int(input("How long have Buzz played ?: "))
hr = min//60
exmin = min%60
price = 0
#print(f"before  {hr}")
#print(exmin)
if exmin>20:
  hr = hr+1
#print(f"after {hr}")
if 0<=hr<2:
  price=hr*900
elif 2<=hr<4:
  price=(hr*900)*90/100
elif 4<=hr<5:
  price=(hr*900)*80/100
elif 5<=hr:
  price=(hr*900)*70/100
print(f"Total price is {price:.0f} baht.")