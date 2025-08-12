class Shape:
    def __init__(self,name):
        self.name=name

    def describe(self):
        print(f"This shape is called {self.name}")
#shape1=Shape(name"")
#shape1=Shape(name="name")
#shape1.describe()

class Rectangle(Shape):
    def __init__(self, length,width):
        super().__init__("Rectangle")
        self.length=length
        self.width=width

    def area(self):
        a=self.width*self.length
        print(f"For {self.name}, the area is {a}")
        return a
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius=radius

    def area(self):
        a=3.142*self.radius*self.radius
        print(f"For {self.name} area is {a}")
        return a
    

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base=base
        self.height=height



r1=Rectangle(20,9)
r1.describe()
r1.area()

c1=Circle(27)
c1.describe()
c1.area()

t1=Triangle(10, 5)
t1.describe()
t1.area()
