import csv
#fn='/tmp/Cities.csv'
fn=input("Enter file name: ")
max=-999999
min=999999
avg=0
overall=0
i=0
with open(fn) as f:
    s=csv.DictReader(f)
    for city in s:
      if float(city['temperature']) > max:
        max=float(city['temperature'])
      elif float(city['temperature']) < min:
        min=float(city['temperature'])
      i+=1
      overall+=float(city['temperature'])
    print(f'Minimum: {min:.2f}')
    print(f'Maximum: {max:.2f}')
    print(f'Average temperature: {overall/i:.4f}')