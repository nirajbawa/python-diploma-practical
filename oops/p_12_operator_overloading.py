class Person:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def __add__(self, x):
        return self.a+x.b+ self.b+x.b

p1 = Person(10, 20)
p2 = Person(10, 20)
print(p1+p2)

