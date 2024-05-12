class Person:
    name = ""
    def pritnVals(self):
        print("hello")
    
class Developer(Person):
    specailize = ""
    def setVals(self, name, specailize):
        self.name = name
        self.specailize = specailize
    
    def printVals(self):
        print(self.name)
        print(self.specailize)
        Person.pritnVals(self)

o = Developer()
o.setVals("niraj", "sde")
o.printVals()