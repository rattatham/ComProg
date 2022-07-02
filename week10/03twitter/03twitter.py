import json
def readfile(fn):
  with open(fn) as f:
    s=f.read()
    s=json.loads(s)
  return s

def two(py):
  users=[]
  count=0
  for user in py:
    if user['author'] not in users:
     # print(count)
      users.append(user['author'])
      count+=1
  return count

def three(py):
  x=0
  users=[]
  times=[]
  for user in py:
    if user['author'] not in users:
      users.append(user['author'])
      times.append(1)
    else:
      index=users.index(user['author'])
      times[index]+=1
  x=max(times)
  for i in range(len(times)):
    if times[i]==x:
      #print(x)
      print(users[i])
  #return users[ind]

def four(py):
  topics=[]
  count=0
  for user in py:
    if user['topic'] not in topics:
      topics.append(user['topic'])
      count+=1
  return count

def five(py):
  count=0
  for user in py:
    if user['topic_priority']=='ALERT':
      count+=1
  return count

def six(py):
  count=0
  for user in py:
    if user['topic_priority']=='UNIMPORTANT':
      count+=1
  return count

def seven(py):
  for user in py:
    if user['language'] != 'EN':
      return True
  return False

def eight(py):
  mymax=-999999
  for user in py:
    text=[words for words in user['text'].split()]
    textnum=len(text)
    if textnum>mymax:
      mymax=textnum
  return mymax


#fn='/tmp/twitter.json'
fn=input('File name: ')
py = readfile(fn)
n=int(input('input: '))
if n==1:
  print(len(py))
elif n==2:
  print(two(py))
elif n==3:
  three(py)
elif n==4:
  print(four(py))
elif n==5:
  print(five(py))
elif n==6:
  print(six(py))
elif n==7:
  print(seven(py))
elif n==8:
  print(eight(py))