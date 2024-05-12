class MyClass:
    def __init__(self, value) -> None:
        self.__value = value
    
    def show(self):
        print("value : ", self.__value)
    
    @property
    def ten_val(self):
        return self.__value
    
    @ten_val.setter
    def ten_val(self, value):
        self.__value = value
    

m = MyClass(10)
print(m.ten_val)
m.ten_val = 20
m.show()
