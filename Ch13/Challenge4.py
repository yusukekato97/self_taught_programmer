# Challenge 4

class Horse:
    def __init__(self, n, r):
        self.name = n
        self.rider = r

class Rider:
    def __init__(self, n):
        self.name = n

makis = Rider("Makisima")
makib = Horse("Makibao", makis)
print(makib.rider.name)
