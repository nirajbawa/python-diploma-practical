class Animal:
    def __init__(self, name):
        self.name = name;
    def eat(self, food):
        print("i eat "+food)
    def ani_name(self):
        print("my name is : "+self.name)
    
class Harbihours(Animal):
    def __init__(self, name, type):
        super().__init__(name)
        self.eat("bread") 
        Animal.eat(self, "bread") 



cat = Harbihours("niraj", "cat")
cat.eat("bread") 
     
cat.ani_name()