class Person:
    name = ""
    lname = ""
    def printVal(self):
        print("name : ",self.name, self.lname)
        
p1 = Person()
p1.name = "niraj"
p1.lname = "bava"
p1.printVal()


p2 = Person()
p2.name = "ram"
p2.lname = "gosavi"
p2.printVal()