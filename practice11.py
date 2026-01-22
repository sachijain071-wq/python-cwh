# # # for i in range(1,20):
# # #     if i % 3 ==0 :
# # #         print("Fizz")
# # #     elif i % 5==0:
# # #         print("Buzz")
# # #     elif i % 3 ==0 and i % 5==0:
# # #         print("FizzBuzz")
# # #     else:
# # #         print(i)

# # # def count_even(numbers):
# # #     count = 0
# # #     for num in numbers:
# # #         if num %2 == 0:
# # #             count += 1
# # #     return count 
    
# # # print(count_even([1,2,3,4,5,8]))

# # def cal_total(price, quantity):
# #     total=price*quantity
# #     if quantity > 10:
# #         total*= 0.9
# #     return total

# # print(cal_total(100,12))

# class Student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks
#     def is_passed(self):
#         if self.marks > 40:
#             return "passed"
#         else:
#             return "failed"
        
# a=Student("dinesh", 45)
# print(a.is_passed())

class BankAccount:
    def __init__(self, owner , balance):
        self.owner=owner
        self.balance=balance 

    def deposit(self, amount):
        self.balance+=amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-= amount
        else:
            print("insufficient balance")

acc=BankAccount("John", 1000)
acc.withdraw(200)
acc.deposit(500)
print(acc.balance)