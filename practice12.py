# # def is_prime(n):
# #     if n <= 1:
# #         return False
# #     for i in range(2, n):
# #         if n % i == 0:
# #             return False
# #     return True

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# def give_bonus(employee):
#     if employee.salary < 50000:
#         employee.salary *= 1.10
#     else:
#         employee.salary *= 1.05

# emp = Employee("Emma", 40000)
# give_bonus(emp)
# print(emp.salary)

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(item)

cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Banana")
cart.show_items()

