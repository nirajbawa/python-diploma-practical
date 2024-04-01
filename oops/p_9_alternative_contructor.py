class Person:
    def __init__(self, name, salary) -> None:
        print(salary, name)
    
    @classmethod
    def fromStr(cls, str):
        return cls(str.split("-")[0], int(str.split("-")[1]))

# p = Person("niraj", 50000)
p = Person.fromStr("niraj-50000")
print(dir(p))
print(p.__dict__)
print(help(p))