
# Inheritance and method overriding

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def speak(self):
        return 'Voice!'

class Dog(Animal):
    def speak(self):
        return 'Woof Woof!'

class Cat(Animal):
    def speak(self):
        return "Meow Meow!"

class Ant(Animal):
    def speak(self):
        return "No Voice!"

a = Ant('Anty', 5)
c = Cat("Catty", 6)
d = Dog("Doggy", 7)

print(f'{a.name} is {a.age} old and speaks {a.speak()}')
print(f'{c.name} is {c.age} old and speaks {c.speak()}')
print(f'{d.name} is {d.age} old and speaks {d.speak()}')  


# This is method overriding