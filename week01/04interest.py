P = int(input("Input principal amount (P): "))
r = float(input("Input annual nominal interest rate (r): "))
n = int(input("Input # of times the interest is compounded per year (n): "))
t = int(input("Input # of years (t): "))
A=P*(1+(r/n))**(n*t)
print(f"Final amount: {A:.2f}")