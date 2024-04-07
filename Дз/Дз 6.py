# Завдання було 1 на вибір а я зробив "2 правильно" та "2 неправильно з нейросітю"



# Завдання 1
# class NoInList(Exception):
#     def __str__(self):
#         return "В списку немає такої людини"

# class People:
#     def __init__(self, name="", age=0):
#         self.name = name 
#         self.age = age
#         self.category = self.get_category()

#     def get_category(self):
#         if self.age < 18:
#             return "Child"
#         elif 18 <= self.age < 50:
#             return "Adult"
#         elif 50 <= self.age <= 65:
#             return "Aged"
#         elif 65 < self.age < 90:
#             return "Old"
#         elif 90 <= self.age:
#             return "Very old"

# Sasha = People("Sasha", 12)
# Katya = People("Katya", 35)
# Nadya = People("Nadya", 56)
# Vova = People("Vova", 71)
# Masha = People("Masha", 89)

# livers = [Sasha, Katya, Nadya, Vova, Masha]

# inp = str(input("Введіть ваше ім'я: "))

# for person in livers:
#     if person.name == inp:
#         print(f"{inp} належить до групи '{person.category}'")
#         break
# else:
#     raise NoInList()


# Завдання 2
# try:
#     number = input("Будь ласка, введіть число: ")
#     number = int(number)
#     print(f"Ваше число: {number}")
# except ValueError:
#     print("Це не вдається конвертувати в число. Будь ласка, спробуйте ще раз.")


# # Завдання 3 Нейросіть допомгала але чомусь помилка 
# from os import *
# try:
#     file_path = input("Будь ласка, введіть шлях до файлу: ")
#     with open(file_path, 'r') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("Файл не знайдено. Будь ласка, перевірте шлях до файлу.")


# Завдання 4 тут теж набуть щось не правильно
# try:
#     from colorama import *

#     try:
#         Fore.colorama()
#     except AttributeError:
#         print("Функцію не вдалося знайти в модулі.")
# except ImportError:
#     print("Модуль не вдалося імпортувати.")

