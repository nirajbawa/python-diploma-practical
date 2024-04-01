from typing import Any


class Person():
    def __len__(self):
        return 10
    def __str__(self) -> str:
        return "hello"
    def __call__(self) -> Any:
        print("hii")
        
p = Person()
p()
print(p)
print(len(p))