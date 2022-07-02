import csv
country=[]
population=[]
fn=input('Enter File name: ')
with open(fn) as f:
  s=csv.reader(f)
  next(s)
  for row in s:
    if row[3] == 'yes' and row[2] =='no':
      country.append(row[0])
      population.append(row[1])
for i in range(len(country)):
  print(country[i],population[i])