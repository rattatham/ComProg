a=input("Row 1 : ").split()
b=input("Row 2 : ").split()
c=input("Row 3 : ").split()
r1=[int(i) for i in a]
r2=[int(i) for i in b]
r3=[int(i) for i in c]
A=[]
A.append(r1)
A.append(r2)
A.append(r3)
#print(r1,r2,r3)
#print(A)
ans=0
ans=A[0][0]*A[1][1]*A[2][2]+A[0][1]*A[1][2]*A[2][0]+A[0][2]*A[1][0]*A[2][1]-A[2][0]*A[1][1]*A[0][2]-A[2][1]*A[1][2]*A[0][0]-A[2][2]*A[1][0]*A[0][1]
print(ans)
