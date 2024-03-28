# Завдання 1 нейросіть допомогла з цим допомога потрібна ДУЖЕ ДОПОМОГла майже все переробив
# class BankAccount:
#     def __init__(self, account_number="", balance=0):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Недостатньо коштів на рахунку")
#             return False
#         else:
#             self.balance -= amount
#             return True

# account = BankAccount()

# while True: 
#     inp = input("Виберіть функцію: ")
#     if inp == "balance":
#         print(account.balance)
#     elif inp == "deposit":
#         amount = int(input("Введіть суму для поповнення: £"))
#         account.deposit(amount)
#     elif inp == "withdraw":
#         amount = int(input("Введіть суму для виведення: £"))
#         account.withdraw(amount)
#     elif inp == "exit":
#         break

# Завдання 2
# class Car:
#     make = ""
#     model = ""
#     year = ""

# car1 = Car
# car1.make = 'Honda'
# car1.model = 'sirvi'
# car1.year = '20/03/21'

# print([car1.make],[car1.model],[car1.year])

# Завдання 3
class Employee:
    name = ""
    position = ""
    salary = 0

people1 = Employee
people1.name = "Bob"
people1.position = "Maneger"
people1.salary = 4000 # В доларах

people2 = Employee
people2.name = "Barbi"
people2.name = "Seller"
people2.salary = 1500

print()