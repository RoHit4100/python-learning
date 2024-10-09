
class Animal:
    legs = 4

cat = Animal()
print(cat.legs)
print(Animal.legs)

# In python there is nothing like private and protected, everything is accessible

class Box:
    # in python constructor is declared using __init__
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    
    
box = Box(4, 6)
print(box.area())

