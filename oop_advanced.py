#Animal sound
class Animal:
    def speak(self):
        print("animal language")
class Dog:
    def speak(self):
        print("Dog Bark")
class Cat:
    def speak(self):
        print("Cat purr")

dog = Dog()
cat = Cat()

#shape
class Shape:
    def __init__(self,b,h):
        self.base = b
        self.height = h
        
    

class Circle(Shape):
    def __init__(self,r):
        self.radius =r
    def area(self):
        print(f"Circle area= {(22/7)*self.radius:.2f}")
    def __str__(self):
        return f"Circle -> radius: {self.radius}"


class Rectangle(Shape):
    def __init__(self, b, h):
        super().__init__(b, h)
    def area(self):
        print(f"Rectangle area= {self.base * self.height}")
    def __str__(self):
        return f"Rectangle -> base: {self.base}, height: {self.height}"

rectangle = Rectangle(24,12)
circle = Circle(12)
print(rectangle)
rectangle.area()
print(circle)
circle.area()

#loop
for i in (dog,cat):
    i.speak()


