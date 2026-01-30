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
