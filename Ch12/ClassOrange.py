
class Orange:
    def __init__(self, w, c):
        '''wegihtはグラム'''
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created")

    def rot(self, days, temp):
        """tempは摂氏"""
        self.mold = days * temp


or1 = Orange(10, "dark orange")
print(or1)
print(or1.weight)
print(or1.color)

or1.weight = 100
or1.color = "light orange"
print(or1.weight)
print(or1.color)

or2 = Orange(4, "dark orange")
or3 = Orange(14, "yellow")

orange = Orange(300, "orange")
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)
