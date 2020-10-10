# Challenge 2

import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * self.radius ** 2

circle1 = Circle(5)
print(circle1.area())
