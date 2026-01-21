class person:
    def __init__(self,name , age):
        self.name=name
        self.age=age
    
    def greet(self):
        print("hello" , self.name)

result=person("kiki", 22)
result.greet()

class BankAcc:
    def __init__(self, acc_holder, balance):
        self.acc_holder= acc_holder
        self.balance= balance

    def greete(self):
        print(f" hye {self.acc_holder} your balance is {self.balance}")


answer=BankAcc("kiki",300000)
answer.greete()
        