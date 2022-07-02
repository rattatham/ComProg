def readfile(fname):
  f=open(f"{fname}","r")
  s=f.read()
  log=[x for x in s.split("\n")]
  for i in range(len(log)):
    log[i]=log[i].split(",")
  for i in range(1,len(log)-1):
    for j in range(0,len(log[i])-1):
      log[i][j]=int(log[i][j])
  f.close()
  return log

# def readfile(fname):
#   with open(fname) as f:
#     s=f.read()
#     log=[x for x in s.split("\n")]
#     for i in range(len(log)):
#       log[i]=log[i].split(",")
#   for i in range(1,len(log)-1):
#     for j in range(0,len(log[i])-1):
#       log[i][j]=int(log[i][j])

  #return log
def one(m):
  return print(len(log)-1)

def two(a,b):
  name=['tvshow',
 'supachalasai',
 'sinthorn',
 'social',
 'food',
 'blueplanet',
 'bangrak',
 'siam',
 'ratchada',
 'isolate',
 'silom',
 'home',
 'lumpini',
 'wahkor',
 'beauty',
 'library',
 'chalermthai',
 'korea',
 'mbk',
 'family',
 'chalermkrung',
 'siliconvalley',
 'klaibann',
 'region',
 'cartoon',
 'jatujak',
 'rajdumnern',
 'horoscope',
 'religious',
 'gallery',
 'theoldsiam',
 'camera',
 'gadget',
 'greenzone',
 'art',
 'writer',
 'pantip']
  all = [tvshow,supachalasai,sinthorn,social,food,blueplanet,bangrak,siam,ratchada,isolate,silom,home,lumpini,wahkor,beauty,library,chalermthai,korea,mbk,family,chalermkrung,siliconvalley,klaibann,region,cartoon,jatujak,rajdumnern,horoscope,religious,gallery,theoldsiam,camera,gadget,greenzone,art,writer,pantip]
  for i in range(len(all)):
    all[i]=sum(all[i])
  for i in range(len(all)):
    for j in range(len(all)):
      if all[i]>all[j]:
        tmp=all[i]
        all[i]=all[j]
        all[j]=tmp
        tmp=name[i]
        name[i]=name[j]
        name[j]=tmp
  return print(name[0])

def three(a,b,blue='blueplanet'):
  blueplanet.sort()
  blueplanet.reverse()
  return print(f"{blueplanet[0]} {blueplanet[1]} {blueplanet[2]}")

def four(a,b,c):
  nuser=-1
  mymax=-9999999
  sum=0
  for usernumber in range(1,len(log)):
    sum=0
    for room in range(len(log[usernumber])-1):
      sum+=log[usernumber][room]
    if sum>mymax:
      mymax=sum
      nuser=usernumber
  return print(log[nuser][37],mymax)

def five(a,b,c,d='tvshow'):
  nuser=-1
  mymax=-9999999
  for usernumber in range(1,len(log)-1):
    sum=0
    sum+=log[usernumber][0]
    if sum>mymax:
      mymax=sum
      nuser=usernumber
  return print(f"{log[nuser][37]} {mymax}")

def six(a,b,k='korea',top=500):
  koreareader=[]
  for usernumber in range(1,len(log)-1):
    if log[usernumber][17] > 500:
      koreareader.append(log[usernumber][37])
  return print(len(koreareader))

def seven(a,b,s='siam',f='food'):
  smtf=[]
  siam=7
  food=4
  for usernumber in range(1,len(log)-1):
    if log[usernumber][siam]>log[usernumber][food]:
      smtf.append(log[usernumber][37])
  return print(len(smtf))

def eight(a,b,c,d='rajdumnern'):
  rajdumnern=26
  nuser=-1
  ratio=0
  for usernumber in range(1,len(log)-1):
    view=0
    for room in range(len(log[usernumber])-1):
      view+=log[usernumber][room]
    ratio1=log[usernumber][rajdumnern]/view
    if ratio1>ratio:
      ratio=ratio1
      nuser=usernumber
    #print(usernumber,ratio1)
  return print(log[nuser][37])

def nine(a,p=70):
  member=0
  for usernumber in range(1,len(log)-1):
    view=0
    userid=log[usernumber].copy()
    mst,sumuserid=mosttwo(userid)
    view=sumuserid
    ratio=mst/view
    if ratio>0.7:
      member+=1
  return print(member)

def ten(a,b,c='pantip'):
  nopantip=0
  for usernumber in range(1,len(log)-1):
    if log[usernumber][36]==0:
      nopantip+=1
  return print(nopantip)

def mosttwo(userid_list):
  maxtwo=0
  userid_list.pop()
  userid_list.sort()
  userid_list.reverse()
  x=sum(userid_list)
  maxtwo=userid_list[0]+userid_list[1]
  return maxtwo,x




user=[]
tvshow=[]
supachalasai=[]
sinthorn=[]
social=[]
food=[]
blueplanet=[]
bangrak=[]
siam=[]
ratchada=[]
isolate=[]
silom=[]
home=[]
lumpini=[]
wahkor=[]
beauty=[]
library=[]
chalermthai=[]
korea=[]
mbk=[]
family=[]
chalermkrung=[]
siliconvalley=[]
klaibann=[]
region=[]
cartoon=[]
jatujak=[]
rajdumnern=[]
horoscope=[]
religious=[]
gallery=[]
theoldsiam=[]
camera=[]
gadget=[]
greenzone=[]
art=[]
writer=[]
pantip=[]

# for i in range(1,len(log)-1):
#   for j in range(0,len(log[i])-1):
#     log[i][j]=int(log[i][j])



fname=input("File name: ")
log=readfile(fname)
for i in range(1,len(log)-1):
  tvshow.append(log[i][0])
  supachalasai.append(log[i][1])
  sinthorn.append(log[i][2])
  social.append(log[i][3])
  food.append(log[i][4])
  blueplanet.append(log[i][5])
  bangrak.append(log[i][6])
  siam.append(log[i][7])
  ratchada.append(log[i][8])
  isolate.append(log[i][9])
  silom.append(log[i][10])
  home.append(log[i][11])
  lumpini.append(log[i][12])
  wahkor.append(log[i][13])
  beauty.append(log[i][14])
  library.append(log[i][15])
  chalermthai.append(log[i][16])
  korea.append(log[i][17])
  mbk.append(log[i][18])
  family.append(log[i][19])
  chalermkrung.append(log[i][20])
  klaibann.append(log[i][21])
  siliconvalley.append(log[i][22])
  region.append(log[i][23])
  cartoon.append(log[i][24])
  jatujak.append(log[i][25])
  rajdumnern.append(log[i][26])
  horoscope.append(log[i][27])
  religious.append(log[i][28])
  gallery.append(log[i][29])
  theoldsiam.append(log[i][30])
  camera.append(log[i][31])
  gadget.append(log[i][32])
  greenzone.append(log[i][33])
  art.append(log[i][34])
  writer.append(log[i][35])
  pantip.append(log[i][36])
  user.append(log[i][37])
n=int(input("enter number: "))

if n==1:
  one(1)
elif n==2:
  two(1,2)
elif n==3:
  three(1,2,blue='blueplanet')
elif n==4:
  four(1,2,3)
elif n==5:
  five(1,2,3,d='tvshow')
elif n==6:
  six(2,1,k='korea',top=500)
elif n==7:
  seven(1,2,s='siam',f='food')
elif n==8:
  eight(1,2,1,d='rajdumnern')
elif n==9:
  nine(1,p=70)
elif n==10:
  ten(1,2,c='pantip')

# while True:
#   n=int(input("enter number: "))
#   if n==0:
#     break
#   if n==1:
#     one(1)
#   elif n==2:
#     two(1,2)
#   elif n==3:
#     three(1,2,blue='blueplanet')
#   elif n==4:
#     four(1,2,3)
#   elif n==5:
#     five(1,2,3,d='tvshow')
#   elif n==6:
#     six(2,1,k='korea',top=500)
#   elif n==7:
#     seven(1,2,s='siam',f='food')
#   elif n==8:
#     eight(1,2,1,d='rajdumnern')
#   elif n==9:
#     nine(1,p=70)
#   elif n==10:
#     ten(1,2,c='pantip')

