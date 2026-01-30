# # 

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side

# s = Square(4)
# print(s.area())

class Bird:
    def fly(self):
        print("Bird flies using wings")

class Airplane:
    def fly(self):
        print("Airplane flies using engines")

def make_fly(obj):
    obj.fly()

make_fly(Bird())
make_fly(Airplane())
