import csv
#fn1='/tmp/Cities.csv'
#fn2='/tmp/Countries.csv'
fn1=input('Enter city file: ')
fn2=input('Enter country file: ')
condit=[]
temp=[]
citynum=[]


with open(fn2) as country_reader:
  countries=csv.DictReader(country_reader)
  for country in countries:
    if country['coastline']=='yes' and country['EU']=='no':
      condit.append(country['country'])
      temp.append(0)
      citynum.append(0)
    
with open(fn1) as city_reader:
  cities=csv.DictReader(city_reader)
  for city in cities:
    for i in range(len(condit)):
      if city['country']==condit[i]:
        #print(city['city'],(city['country']))
        temp[i]+=float(city['temperature'])
        citynum[i]+=1

print('Average temperature of countries having coastline, but not in EU: ')
for i in range(len(condit)):
  if citynum[i]!=0:
    print(condit[i],f'{temp[i]/citynum[i]:.2f}')