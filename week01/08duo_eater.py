S = int(input("Input starting food (S): "))
P = int(input("Input Paun's eating rate (P): "))
n = int(input("Input Gane's eating rate (n): "))
PE=S//P
nE=(S-PE*P)//n
dog=S-(PE*P)-(nE*n)
print(f"Paun eats {PE} time(s)")
print(f"Gane eats {nE} time(s)")
print(f"Remaining {dog} for dog")
