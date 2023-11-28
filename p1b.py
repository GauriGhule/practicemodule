from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        a=3.14*self.radius**2
        print("Area of circle is",a)

    def perimeter(self):
        b = 2*3.14*self.radius
        print("Perimeter of circle is", b)

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        b= self.side**2
        print("Area of square is",b)

    def perimeter(self):
        c=self.side*4
        print("Perimeter of square is",c)

while True:
    print("\n Main menu \n 1. Circle\n 2.Square")
    choice1 = int(input("Enter the choice:"))
    if choice1==1:
        a = int(input("Enter the radius"))
        obj= Circle(a)
    elif(choice1==2):
       b = int(input("Enter the side"))
       obj= Square(b) 
    j = int(input("\n Select operation \n 1.calculate area \n 2. perimeter"))
    if (j==1):
        obj.area()
    elif(j==2):
        obj.perimeter()
    else:
        print("Incorrect input\n")

