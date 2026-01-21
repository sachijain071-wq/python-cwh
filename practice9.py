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



class Cal:
    def __init__(self, n):
        self.n=n 

    def square(self):
        print(f" the square is {self.n*self.n}")

    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")

res=Cal(4)
res.square()
res.cube()
        


    