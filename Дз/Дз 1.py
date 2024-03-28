# Завдання 3_1
# name = input("Введіть ваше ім'я: ")
# age = input("Введіть ваш вік: ")
# print(f"Привіт {name}, тобі {age} років")

# Завдання 3_2
# age = int(input("Введіть ваш вік: "))
# if age < 18:
#     print("Вхід заборонено!")
# else:
#     print("Вхід дозволено!")

# Завдання 3_3
# import random
# rand_num = random.randint(1, 10)
# am = int(input("Яке число я загадав(від 1 до 10)? "))
# while True:
#     am = int(input("Спробуйте ще раз: "))
#     if am > rand_num:
#         print("Воно менше")
#     elif am < rand_num:
#         print("Воно більше")
#     elif am == rand_num:
#         print("Ура ви вгадали число")
#         break

# Завдання 3_4
# a = int(input("Введіть перше число:"))
# b = int(input("Введіть друге число:"))

# def print_numbers_between(a, b):
#     for i in range(a+1, b):
#         print(i)

# print_numbers_between(a, b)

# Завдання 3_5_1 тут я вже в інтернеті допомогу знайшов ну топто цей код
# n = int(input("Введіть число для факторіалу: "))
# factorial = 1
# for i in range(2, n+1):
#     factorial *= i
# print(factorial)

# Завдання 3_5_2 тут навіть паритися не треба
# a = int(input("Введіть число для факторіалу: "))
# import math
# m = math.factorial(a)
# print(m)

# Завдання 3_6
# while True:
#     bal = int(input("Введіть отриманий вами бал: "))
#     if bal < 50:
#         print("Незадовільно")
#     elif 50 <= bal < 70:
#         print("Задовільно")
#     elif 70 <= bal < 90:
#         print("Добре")
#     elif 90 <= bal < 101:
#         print("Відмінно")
#         break

# Завдання 3_7
# a = int(input("Введіть перше число: "))
# c = input("Введіть дію(/,*,+,-): ")
# b = int(input("Введіть друге число: "))

# if b == 0 and c == "/":
#     print("Ділення на нуль неможливо")
# else:
#     if c == "+":
#         print("Результат:", a + b)
#     elif c == "-":
#         print("Результат:", a - b)
#     elif c == "*":
#         print("Результат:", a * b)
#     elif c == "/":
#         print("Результат:", a / b)
#     else:
#         print("Невідома дія")
