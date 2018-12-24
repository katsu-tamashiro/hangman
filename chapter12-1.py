import math

class Circle:
    def __init__(self,r):
        self.radius = r


    def area(self):
        return self.radius ** 2 * math.pi


circle1 = Circle(3)
print (circle1.radius)
print (circle1.area())


