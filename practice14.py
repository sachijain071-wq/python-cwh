# class Parent:
#     def display(self):
#         print("Parent display")

# class Child(Parent):
#     def display(self):
#         print("Child display")

# obj = Child()
# obj.display()

class A:
    def show_a(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

class C(B):
    def show_c(self):
        print("Class C")

obj = C()
obj.show_a()
obj.show_b()
obj.show_c()
