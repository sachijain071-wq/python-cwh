# class person:
#     def __init__(self,name , age):
#         self.name=name
#         self.age=age
    
#     def greet(self):
#         print("hello" , self.name)

# result=person("kiki", 22)
# result.greet()

# class BankAcc:
#     def __init__(self, acc_holder, balance):
#         self.acc_holder= acc_holder
#         self.balance= balance

#     def greete(self):
#         print(f" hye {self.acc_holder} your balance is {self.balance}")


# answer=BankAcc("kiki",300000)
# answer.greete()

class Cal:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    # def value(self, length, breadth):
    #     self.length= length
    #     self.breadth= breadth

    def area(self):
        print(f"the area of rect is {self.x * self.y}")

    def perimeter(self):
        print(f" the perimeter of rect is {2* (self.x+ self.y)}")

res=Cal(2,3)
res.area()
res.perimeter()
        