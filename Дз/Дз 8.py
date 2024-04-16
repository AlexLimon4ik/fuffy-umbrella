# Завдання 1
# import logging
# import random

# logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s")
# logging.info('The program is working')

# class Human:
#     def __init__(self, name="Human", job=None, home=None, car=None):
#         logging.info('Initializing Human')
#         self.name = name
#         self.money = 100
#         self.gladness = 50
#         self.satiety = 50
#         self.job = job
#         self.car = car
#         self.home = home

#     def get_home(self):
#         logging.info('Getting home')
#         self.home = House()

#     def get_car(self):
#         logging.info('Getting car')
#         self.car = Auto(brands_of_car)

#     def get_job(self):
#         logging.info('Getting job')
#         if self.car.drive():
#             pass
#         else:
#             self.to_repair()
#             return
#         self.job = Job(job_list)

#     def eat(self):
#         logging.info('Eating')
#         if self.home.food <= 0:
#             self.shopping("food")
#         else:
#             if self.satiety >= 100:
#                 self.satiety = 100
#                 return
#             self.satiety += 5
#             self.home.food -= 5

#     def work(self):
#         logging.info('Working')
#         if self.car.drive():
#             pass
#         else:
#             if self.car.fuel < 20:
#                 self.shopping("fuel")
#                 return
#             else:
#                 self.to_repair()
#                 return
#             self.money += self.job.salary
#             self.gladness -= self.job.gladness_less
#             self.satiety -= 4

#     def shopping(self, manage):
#         logging.info('Shopping')
#         if self.car.drive():
#             pass
#         else:
#             if self.car.fuel < 20:
#                 manage = "fuel"
#             else:
#                 self.to_repair()
#                 return
#         if manage == "fuel":
#             print("I bought fuel")
#             self.money -= 100
#             self.car.fuel += 100
#         elif manage == "food":
#             print("Bought food")
#             self.money -= 50
#             self.home.food += 50
#         elif manage == "delicacies":
#             print("Hooray! Delicious!")
#             self.gladness += 10
#             self.satiety += 2
#             self.money -= 15

#     def chill(self):
#         logging.info('Chilling')
#         self.gladness += 10
#         self.home.mess += 5

#     def clean_home(self):
#         logging.info('Cleaning home')
#         self.gladness -= 5
#         self.home.mess = 0

#     def to_repair(self):
#         logging.info('Repairing')
#         self.car.strength += 100
#         self.money -= 50

#     def days_indexes(self, day):
#         logging.info('Getting day indexes')
#         day = f" Today the {day} of {self.name} 's life "
#         print(f"{day:=^50}", "\n")
#         human_indexes = self.name + "'s indexes"
#         print(f"{human_indexes:^50}", "\n")
#         print(f"Money – {self.money}")
#         print(f"Satiety – {self.satiety}")
#         print(f"Gladness – {self.gladness}")
#         home_indexes = "Home indexes"
#         print(f"{home_indexes:^50}", "\n")
#         print(f"Food – {self.home.food}")
#         print(f"Mess – {self.home.mess}")
#         car_indexes = f"{self.car.brand} car indexes"
#         print(f"{car_indexes:^50}", "\n")
#         print(f"Fuel – {self.car.fuel}")
#         print(f"Strength – {self.car.strength}")

#     def is_alive(self):
#         logging.info('Checking if alive')
#         if self.gladness < 0:
#             print("Depression...")
#             return False
#         if self.satiety < 0:
#             print("Dead...")
#             return False
#         if self.money < -500:
#             print("Bankrupt...")
#             return False

# class Auto:
#     def __init__(self, brand_list):
#         logging.info('Initializing Auto')
#         self.brand = random.choice(list(brand_list))
#         self.fuel = brand_list[self.brand]["fuel"]
#         self.strength = brand_list[self.brand]["strength"]
#         self.consumption =brand_list[self.brand]["consumption"]

#     def drive(self):
#         logging.info('Driving')
#         if self.strength > 0 and self.fuel >= self.consumption:
#             self.fuel -= self.consumption
#             self.strength -= 1
#             return True
#         else:
#             print("The car cannot move")
#             return False

# class House:
#     def __init__(self):
#         logging.info('Initializing House')
#         self.mess = 0
#         self.food = 0

# job_list = {
# "Java developer":
# {"salary":50, "gladness_less": 10 },
# "Python developer":
# {"salary":40, "gladness_less": 3 },
# "C++ developer":
# {"salary":45, "gladness_less": 25 },
# "Rust developer":
# {"salary":70, "gladness_less": 1 },
# }

# brands_of_car = {
# "BMW":{"fuel":100, "strength":100,
# "consumption": 6},
# "Lada":{"fuel":50, "strength":40,
# "consumption": 10},
# "Volvo":{"fuel":70, "strength":150,
# "consumption": 8},
# "Ferrari":{"fuel":80, "strength":120,
# "consumption": 14},
# }

# class Job:
#     def __init__(self, job_list):
#         logging.info('Initializing Job')
#         self.job = random.choice(list(job_list))
#         self.salary = job_list[self.job]["salary"]
#         self.gladness_less = job_list[self.job]["gladness_less"]

# nick = Human(name="Nick")
# for day in range(100):
#     logging.info('Living day: {}'.format(day))
#     if nick.live(day) == False:
#         break


# Завдання 2
# import time

# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Час виконання функції {func.__name__}: {end_time - start_time} секунд")
#         return result
#     return wrapper

# @timer_decorator
# def test_function(n):
#     sum = 0
#     for i in range(n):
#         sum += i
#     return sum

# # Тестуємо нашу функцію
# print(test_function(1000000))


# Додаткове завдання 
# import time
# import logging
# from functools import wraps

# # Налаштування логування
# logging.basicConfig(level=logging.ERROR)

# def error_logger_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             logging.error(f"Помилка виконання функції '{func.__name__}': {str(e)}")
#             raise e
#     return wrapper

# def timer_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Час виконання функції '{func.__name__}': {end_time - start_time} секунд")
#         return result
#     return wrapper

# @error_logger_decorator
# @timer_decorator
# def test_func(n):
#     return sum(i*i for i in range(n))

# try:
#     print(test_func(10000))
#     print(test_func('a'))  # це викличе помилку
# except Exception as e:
#     pass
