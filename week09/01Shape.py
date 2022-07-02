class Rectangle:
  def __init__(self,length,width):
    self.length=length
    self.width=width
  def area(self):
    area=self.width*self.length
    return area
  def perimeter(self):
    perimeter=2*(self.width+self.length)
    return perimeter
  def is_square(self):
    if self.width==self.length:
      return "This rectangle is square too."
    else:
      return "This rectangle is not square."
  # def __str__(self):
  #   return 'l = ' +self.length +' / w = ' +self.width

class Triangle:
  def __init__(self,l1,l2,l3):
    self.l1=l1
    self.l2=l2
    self.l3=l3
  def area(self):
    s=(self.l1+self.l2+self.l3)/2
    area = (s*(s-self.l1)*(s-self.l2)*(s-self.l3))**.5
    return area
  def is_right_triangle(self):
    L=[]
    L.append(self.l1)
    L.append(self.l2)
    L.append(self.l3)
    L.sort()
    L.reverse()
    if L[0]**2 == L[1]**2+L[2]**2:
      return "This triangle is right triangle too."
    else:
      return "This triangle is not right triangle."
  def perimeter(self):
    perimeter=self.l1+self.l2+self.l3
    return perimeter

class Circle:
  def __init__(self,radius):
    self.radius=radius
  def area(self):
    area=3.14*self.radius**2
    return area
  def perimeter(self):
    perimeter=2*3.14*self.radius
    return perimeter


l = int(input("Enter rectangle length : "))  
w = int(input("Enter rectangle width : "))  
p1 = Rectangle(l,w)  
print(f'Area is {p1.area()}.')  
print(f'Perimeter is {p1.perimeter()}.')  
print(p1.is_square()) 

l1 = int(input("Enter triangle first side length : "))  
l2 = int(input("Enter triangle second side length : "))  
l3 = int(input("Enter triangle third side length : "))  
p2 = Triangle(l1,l2,l3)  
print(f'Area is {p2.area()}.')  
print(f'Perimeter is {p2.perimeter()}.')  
print(p2.is_right_triangle()) 

r = int(input("Enter circle radius : "))  
p3 = Circle(r)  
print(f'Area is {p3.area()}.')  
print(f'Perimeter is {p3.perimeter()}.')  