class Rectangle:
    def __init__(self, width, height) -> None:
        self.width= width
        self.height = height
    def area(self):
        print(self.width*self.height)
        
class Circle(Rectangle):
    def __init__(self, width, height, radius) -> None:
        self.radius = radius
        super().__init__(width, height)
    def area(self):
        print(3.14*(self.radius*self.radius))
        super().area()

ob = Circle(10, 20, 20)
ob.area()
