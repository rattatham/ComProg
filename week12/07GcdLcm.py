def gcd(a,b):
  if b==0:
    return a
  return gcd(b,a%b)
a=int(input('a : '))
b=int(input('b : '))
print('GCD :',gcd(a,b))
print("LCM :",int(a*b/gcd(a,b)))