def rad(r):
  radian=r*3.14/180
  return radian

def fact(i):
  a=0
  fac=1
  for a in range(a,i+1):
    if a==0:
      fac*=1   
    elif a==1: 
      fac*=1 
    elif a>=1:
      fac*=a
  return fac

def cosin(x):
  cos=0
  for y in range(0,11):
    cos+=((-1)**y)*x**(2*y)/(fact(2*y))
  return cos

def sine(c):
  sin=0
  for z in range(1,11):
    sin+=((-1)**(z-1))*(c**(2*z-1))/fact(2*z-1)
  return sin

n=float(input("degree: "))
print(f"sin({n:.2f}): {sine(rad(n)):.10f}")
print(f"cos({n:.2f}): {cosin(rad(n)):.10f}")