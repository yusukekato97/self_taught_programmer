# Challenge 3

def is_same_object(a, b):
    if a is b:
        return  True
    else:
        return False

class TestClass:
    def __init__(self):
        pass

t1 = TestClass()
t2 = t1
t3 = TestClass()

print(is_same_object(t1, t2))
print(is_same_object(t1, t3))

t4 = "Terminator".lower()
t5 = "terminator"
t6 = t4
print(is_same_object(t4, t5))
print(is_same_object(t4, t6))
