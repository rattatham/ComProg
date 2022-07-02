N=int(input("N: "))
M=int(input("M: "))
p=[]
q=[]
for i in range(1,N+1):
  a=int(input((f"Input number {i}: ")))
  n=a%M
  if n not in p:
    p.append(n)
    q.append(1)
print(len(q))