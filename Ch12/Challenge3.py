# Challenge 3

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.base * self.height / 2

triangle1 = Triangle(15, 8)
print(triangle1.area())
