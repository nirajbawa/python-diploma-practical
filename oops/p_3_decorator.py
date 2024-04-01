def greet(fx):
    def mfx(*args, **kwargs):
        print("welcome")
        fx(*args, **kwargs)
        print("byy")
    return mfx


@greet
def add(a, b):
    print(a+b)
    
add(10, 20)