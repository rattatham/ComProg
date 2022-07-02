def zigzag(n):
    def compare(xy):
        #print(xy)
        x, y = xy
        return (x + y, -y if (x + y) % 2 else y)
    xs = range(n)
    return {index: n for n, index in enumerate(sorted(
        ((x, y) for x in xs for y in xs),
        key=compare
    ))}
 
 
def printzz(myarray):
    n = int(len(myarray) ** 0.5 + 0.5)
    xs = range(n)
    x=str(print('\n'.join(
        [''.join("%3i" % myarray[(x, y)] for x in xs) for y in xs]
    )))
    return x

def printmat(mat2):
  for i in range(len(mat2)-1,-1,-1):
    for j in range(len(mat2[i])-1,-1,-1):
      print(f'{mat2[j][i]:3.0f}',end=' ')
    print()


n=int(input(""))
x=zigzag(n)
#print(x.keys())
mat=[]
mat2=[]
for i in range(n):
    mat.append([])
i=1
for pos in x.keys():
    mat[pos[0]].append(i)
    i+=1
for i in range(len(mat)):
    mat2.append(mat[-i-1])

#print(mat2)
printmat(mat2)
