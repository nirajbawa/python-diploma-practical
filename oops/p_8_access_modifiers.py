class Person():
    def __init__(self):
        self.__name = "niraj"
        self._lname = ""

class developer(Person):
    def __init__(self):
        super().__init__()
        self.__lname = "bava"


p = developer()
# p.__name = "bava"
print(p._Person__name)
# print(p.__lname)
# print(p.__name)

print(dir(p))