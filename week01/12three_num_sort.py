A = int(input(""))
B = int(input(""))
C = int(input(""))
if A>B>C:
  print(C,B,A)
elif A>C>B:
  print(B,C,A)
elif B>A>C:
  print(C,A,B)
elif B>C>A:
  print(A,C,B)
elif C>A>B:
  print(B,A,C)
elif C>B>A:
  print(A,B,C)

