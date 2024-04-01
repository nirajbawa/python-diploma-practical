class Cal:
    def add(self, a, b, c=None):
        if a!=None and b!=None and c!=None  :
            return a+b+c
        elif a != None and b!=None :
            return a+b
        
c = Cal()
print(c.add(10, 20))
print(c.add(10, 20, 30))