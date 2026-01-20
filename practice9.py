# import random 

# computer=random.choice([1,-1,0])
# youstr=input("enter your choice: ")
# youDict={"s": 1, "w": -1, "g": 0}
# revDict={1: "snake", -1: "water", 0: "gun"}

# you=youDict[youstr]

# print(f" you choose {revDict[you]}\n computer choose{revDict[computer]}")

# if(computer== you):
#     print("its a draw")

# else:
#     if(computer== -1 and you == 1):
#         print("you win")

#     elif(computer == -1 and you ==0):
#         print("you loose")

#     elif(computer == 1 and you == -1):
#         print("you loose")

#     elif(computer == 1 and you ==0):
#         print("you win")

#     elif(computer == 0 and you == -1):
#         print("you win")

#     elif(computer == 0 and you == 1):
#         print("you loose")

#     else:
#         print("somthing went wrong")



class Employee:
    name="kiki"
    language="python"#class attribute

    # def getInfo(self):
    #     print(f"the language is {self.language} and the name is {self.name}")

    def __init__(self, name, language):
            self.name=name
            self.language=language
        

kiki=Employee("kiki", "python")
# kiki.language="JS"#instance attribute
# print(kiki.name)
# print(kiki.language)
print(kiki.name,kiki.language)


    