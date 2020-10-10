# Challenge 1, 2, 3

class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,w,l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

class Square(Shape):
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return 4 * self.side

    def change_size(self, c):
        self.side += c

rec1 = Rectangle(4, 9)
print(rec1.calculate_perimeter())

squ1 = Square(6)
print(squ1.calculate_perimeter())

squ1.change_size(7)
print(squ1.calculate_perimeter())
squ1.change_size(-3)
print(squ1.calculate_perimeter())

rec1.what_am_i()
