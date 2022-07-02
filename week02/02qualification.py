w = int(input("Weight: "))
h = int(input("Height: "))
H=h/100
#print(H)
bmi=w/H**2
#print(bmi)
if bmi>=30:
  print(f"Your BMI is {bmi:.1f} You're in the obese range.")
elif 25<=bmi<30:
  print(f"Your BMI is {bmi:.1f} You're in the overweight range.")
elif 18.6<=bmi<25:
  print(f"Your BMI is {bmi:.1f} You're in the healthy weight range.")
elif bmi<18.6:
  print(f"Your BMI is {bmi:.1f} You're in the underweight range.")