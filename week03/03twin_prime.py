def isPrime(n):
  res = True
  for i in range(2, n//2 + 1):
    if n%i == 0:
      res = False
      break
  return res
n=int(input("N: "))
for x in range(n,n*2,1):
  if isPrime(x) and isPrime(x+2):
      print(f"({x}, {x+2})")
      break
