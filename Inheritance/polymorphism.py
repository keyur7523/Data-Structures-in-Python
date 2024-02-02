
class Calculator:
    def add(self, a:int, b:int):
        return a + b
    def add(self, a:int, b:int, c:int):
        return a + b + c

c = Calculator()
d = Calculator()
print(c.add(1,2,3))
print(d.add(3,4))