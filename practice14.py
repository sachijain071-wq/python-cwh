class Parent:
    def display(self):
        print("Parent display")

class Child(Parent):
    def display(self):
        print("Child display")

obj = Child()
obj.display()
