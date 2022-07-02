s = int(input("s: "))
hr = s//3600
min = (s-hr*3600)//60
sec = s-(hr*3600)-(min*60)
print(f"{s} seconds equals {hr} hour(s) {min} minute(s) and {sec} second(s)")