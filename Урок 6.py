# try:
#     print("Hello")
#     print(10/0)
#     print("No error")
# except (NameError,  ZeroDivisionError):
#     print("We have an NameError")
# print("code after capsule")


# try:
#     num = int(input("Введіть число: "))
#     num += 5
#     print(num)
# except ValueError:
#     print("Ти ввів не число")


# class BuildingError(Exception):
#     def __str__(self):
#         return f"З такої кількості матеріалу будинок не збудувати!"
# def check_material(amounot_of_material, limit_value):
#         if amounot_of_material >= limit_value:
#             return "enoth material"
#         else:
#             raise BuildingError(amounot_of_material)
# materilas = 123
# check_material(materilas, limit_value=300)

# try:
#     numerator = int(input("Введіть чисельник: "))
#     denominator = int(input("Введіть знаменник: "))
#     result = numerator / denominator
#     print("Результат ", result)
# except ZeroDivisionError:
#     print("Помилка: Ділення на нуль неможливе.")
# except ValueError:
#     print("Введені дані не є числом.")