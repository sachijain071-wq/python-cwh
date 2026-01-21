class person:
    def __init__(self,name , age):
        self.name=name
        self.age=age
    
    def greet(self):
        print("hello" , self.name)

result=person("kiki", 22)
result.greet()
