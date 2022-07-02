import csv
countrylis=[]
temp=[]
citynum=[]
#fn='/tmp/Cities.csv'
fn=input('Enter file name: ')
with open(fn) as city_reader:
  cities=csv.DictReader(city_reader)
  for city in cities:
    if city['country'] not in countrylis:
      countrylis.append(city['country'])
      temp.append(0)
      citynum.append(0)
    for i in range(len(countrylis)):
      if countrylis[i]==city['country']:
        temp[i]+=float(city['temperature'])
        citynum[i]+=1
for i in range(len(countrylis)):
  if citynum!=0:
    print(f'{countrylis[i]} {temp[i]/citynum[i]:.2f}')

