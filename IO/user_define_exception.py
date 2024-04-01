class CustomError(Exception):
    def __init__(self, message="A custom error"):
        self.message = message
        super().__init__(self.message)
        
try:
    raise CustomError()
except CustomError as e:
    print(e)
    
try:
    raise CustomError("hello")
except Exception as e:
    print(e)