w = int(input("w: "))
h = int(input("h: "))
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
A=(w*h)-((1/2)*(2*c+2*b)*a)-(2*((1/2)*a*(b+c)))
print(f"Area: {A:.2f}")