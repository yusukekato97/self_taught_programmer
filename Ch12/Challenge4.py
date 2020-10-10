# Challenge 4

class Hexagon:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 6

hexagon1 = Hexagon(21)
print(hexagon1.calculate_perimeter())
