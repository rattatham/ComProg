import math
a=int(input("Input a: "))
b=int(input("Input b: "))
c=int(input("Input c: "))
d=int(input("Input d: "))
e=int(input("Input e: "))
mean=(a+b+c+d+e)/5
sd=math.sqrt(((a-mean)**2+(b-mean)**2+(c-mean)**2+(d-mean)**2+(e-mean)**2)/5)  
print(f"mean: {mean:.3f}")
print(f"sd: {sd:.3f}")