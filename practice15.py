# 
class Vehicle:
    def fuel_type(self):
        print("Uses fuel")

class Car(Vehicle):
    def fuel_type(self):
        print("Uses petrol or diesel")

c = Car()
c.fuel_type()
