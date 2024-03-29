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

# print(f"{car1.make},{car1.model},{car1.year}")

# Завдання 3
# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary

# people1 = Employee("Bob", "Manager", 4000)
# people2 = Employee("Barbi", "Seller", 1500)

# print(f"Заробітна плата {people1.name}: {people1.salary}$")
# print(f"Заробітна плата {people2.name}: {people2.salary}$")

# Завдання 4 в мене тут помилок було капєєєц то нейросіть допомогла(Об'яснила як зробити математику)
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.width * self.height

#     def calculate_perimeter(self):
#         return (self.width + self.height) * 2

# rectangle1 = Rectangle(5, 10)

# print(f"Площа: {rectangle1.calculate_area()}")
# print(f"Периметр: {rectangle1.calculate_perimeter()}")

# Завдання 5
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def calculate_total_price(self):
#         return self.price * self.quantity
    
#     def display_info(self):
#         print(f"Назва: ©{self.name}, Ціна: {self.price}$, Є в наявності: {self.quantity}шт.")
        
# computer1 = Product("MacBook-Pro", 1600, 15)

# while True:
#     inp = input("Введіть функцію: ")
#     if inp == "info":
#         computer1.display_info()
#     if inp == "buy all":
#         print(f"Ціна за 15 MacBook Pro: {computer1.calculate_total_price()}$")
#     if inp == "exit":
#         break