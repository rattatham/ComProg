import json
def readfile(fn):
  dat=[]
  for line in open(fn,'r'):
    dat.append(json.loads(line))
  return dat

def two(py):
  reviewer=[]
  for review in py:
    if review['reviewerID'] not in reviewer:
      reviewer.append(review['reviewerID'])
  return len(reviewer)

def three(py):
  prod=[]
  for review in py:
    if review['productName'] not in prod:
      prod.append(review['productName'])
  return len(prod)

def four(py):
  cate=[]
  for review in py:
    items=[x for x in review['category'].strip().split('>')]
    for i in range(len(items)):
      if items[0] not in cate:
        cate.append(items[0])
  return len(cate)

def five(py):
  cate=[]
  for review in py:
    items=[x for x in review['category'].strip().split('>')]
    for i in range(len(items)):
      if items[1] not in cate:
        cate.append(items[1])
  return len(cate)

def six(py):
  reviewer=[]
  times=[]
  for review in py:
    if review['reviewerID'] not in reviewer:
      reviewer.append(review['reviewerID'])
      times.append(1)
    else:
      rvind=reviewer.index(review['reviewerID'])
      times[rvind]+=1
  x=max(times)
  for i in range(len(times)):
    if times[i]==x:
      print(reviewer[i])

def seven(py):
  mymax=-999
  product=[]
  time=[]
  score=[]
  for review in py:
    if review['productName'] not in product:
      product.append(review['productName'])
      time.append(1)
      score.append(review['overall'])
    else:
      x=product.index(review['productName'])
      time[x]+=1
      score[x]+=review['overall']
  avg=[]
  for i in range(len(score)):
    avg.append(score[i]/time[i])
  x=max(avg)
  tmp1=0
  tmp2=0
  for i in range(len(avg)):
    if avg[i]==x and time[i]>tmp2:
      #print(avg[i],print(time[i]))
      tmp1=i
      tmp2=time[i]
  #print(tmp1)
  #print(tmp2)
  print(product[tmp1])

def eight(py):
  product=[]
  wordnum=[]
  time=[]
  for review in py:
    if review['productName'] not in product:
      product.append(review['productName'])
      wordnum.append(len([word for word in review['reviewText'].split()]))
      time.append(1)
    else:
      ind=product.index(review['productName'])
      time[ind]+=1
      wordnum[ind]+=(len([word for word in review['reviewText'].split()]))
  avg=[]
  for i in range(len(wordnum)):
    avg.append(wordnum[i]/time[i])
  x=max(avg)
  ind=avg.index(x)
  print(product[ind])

#fn='/tmp/amazon1.json'
fn=input('file name: ')
n=int(input('input: '))
py=readfile(fn)
if n==1:
  print(len(py))
elif n==2:
  print(two(py))
elif n==3:
  print(three(py))
elif n==4:
  print(four(py))
elif n==5:
  print(five(py))
elif n==6:
  six(py)
elif n==7:
  seven(py)
elif n==8:
  eight(py)