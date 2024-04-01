class Person:
    name = ""
    
class Developer(Person):
    specailize = ""
    def setVals(self, name, specailize):
        self.name = name
        self.specailize = specailize
    
    def printVals(self):
        print(self.name)
        print(self.specailize)

o = Developer()
o.setVals("niraj", "sde")
o.printVals()