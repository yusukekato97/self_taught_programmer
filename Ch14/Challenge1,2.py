# Challenge 1,2

class Square:
    square_list = []
    
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.square_list.append(self)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.width, self.len, self.width, self.len)

sq1 = Square(1, 3)
sq2 = Square(6, 9)
sq3 = Square(15, 71)

print(Square.square_list)

print(sq1)
print(sq3)
