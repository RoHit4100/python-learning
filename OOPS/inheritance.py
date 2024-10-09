class Animal:
    legs = 4
    eyes = 2
    
    def __init__(self, name):
        self.name = name
    
    # Making speak a method, not a property
    # def speak(self):
    #     raise NotImplementedError

    name = 'animal'
    
    def getLegs(self):
        return self.legs
    
    def getEyes(self):
        return self.eyes
    
    def getName(self):
        return self.name

# Inherited classes should override speak as a method
class Cat(Animal):
    def speak(self):
        return 'meowwwwwww'


class Dog(Animal):
    
    def speak(self, color):
        super().__init__(color)
        print(self.name)
        
        print(super().getName())
        return 'bhowwwwww'

class Duck(Animal):
    def speak(self):
        return 'quak quak'
    
    def name(self):
        return 'badak'
    
    
# Creating instances
dog = Dog('child')
print(dog.speak('orange'))  

cat = Cat('child')
print(cat.getName())

print(dog.getName())