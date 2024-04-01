class MyClass:
    def __init__(self, value) -> None:
        self._value = value
    
    def show(self):
        print("value : ", self._value)
    
    @property
    def ten_val(self):
        return self._value
    
    @ten_val.setter
    def ten_val(self, value):
        self._value = value
    

m = MyClass(10)
print(m.ten_val)
m.ten_val = 20
m.show()