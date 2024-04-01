class Person():
    # class variable
    company = "google"
    def __init__(self):
        self.__name = "niraj"
        self._lname = "bava"
        print(self.company)
        self.changeCp("tesla")
        self.add(5, 5)
    
    @staticmethod
    def add(a, b):
        print(a+b)
    
    @classmethod
    def changeCp(cls, name):
        cls.company = name
        
p = Person()
p.add(20, 10)
Person.add(10, 10)
print(Person.company)
# print(Person._lname)