# Завдання 1 трохи нейроіть допомогла 
# class Human:
#     def __init__(self, name="Human"):
#         self.name = name
#         self.pets = []

#     def add_pet(self, pet):
#         self.pets.append(pet)

#     def print_pets_names(self):
#         if self.pets:
#             print(f"{self.name} has these pets:")
#             for pet in self.pets:
#                 print(pet.name)
#         else:
#             print(f"{self.name} has no pets.")

# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []

#     def add_passenger(self, human):
#         self.passengers.append(human)

#     def print_passengers_names(self):
#         if self.passengers:
#             print(f"Names of {self.brand} passengers:")
#             for passenger in self.passengers:
#                 print(passenger.name)
#         else:
#             print(f"There are no passengers in {self.brand}.")

# class Animal:
#     def __init__(self, name="Animal"):
#         self.name = name

# class Cat(Animal):
#     def __init__(self, name=""):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name=""):
#         self.name = name

# pet1 = Cat("Kiten")
# pet2 = Dog("Dogy")
# Yarik = Human("Yarik")
# Pavlik = Human("Pavlik")
# car = Auto("Ferrari")

# Yarik.add_pet(pet1)
# Pavlik.add_pet(pet2)

# car.add_passenger(Yarik)
# car.add_passenger(Pavlik)

# car.print_passengers_names()
# Yarik.print_pets_names()
# Pavlik.print_pets_names()


# Завдання 2 сам робив
# class Food:
#     def __init__(self, name="food", saturation=0):
#         self.name = name
#         self.saturation = saturation

#     def print_saturation(self):
#         print(f"Насищеня цією їжею: {self.saturation}")

# class Humman:
#     def __init__(self, name="People", satiety=100):
#         self.name = name
#         self.satiety = satiety

#     def working(self):
#         self.satiety = self.satiety - 30
#         print(f"Ой добре попрацював (-30 ситість)")

#     def do_sport(self):
#         self.satiety = self.satiety - 50
#         print(f"М'язи підкачав (-50 ситість)")

#     def go_dacia(self):
#         self.satiety = self.satiety - 90
#         print(f"Фуууух ще трохи і помру з голоду (-90 ситість)")

#     def print_hungry(self):
#         print(f"Ситість {self.name}: {self.satiety}")

#     def hungry(self):
#         if self.satiety < 35:
#             print(f"{self.name} голодний")
#         elif self.satiety > 110:
#             print(f"{self.name} переїв")
#         else:
#             print(f"{self.name} не голодний")

#     def eating_pizza(self):
#         self.satiety = self.satiety + pizza.saturation
#         print(f"{self.name} з'їв {pizza.name} (+70 ситість)")

#     def eating_buger(self):
#         self.satiety = self.satiety + buger.saturation
#         print(f"{self.name} з'їв {buger.name} (+30 ситість)")

#     def eating_cookies(self):
#         self.satiety = self.satiety + cookies.saturation
#         print(f"{self.name} з'їв {cookies.name} (+15 ситість)")

# Buba = Humman("Буба", 100)
# pizza = Food("Піца", 70)
# buger = Food("Бургер", 30)
# cookies = Food("Печиво", 15)


# while True:
#     if Buba.satiety <= 0:
#         print("Він помер від голоду")
#         break
#     elif Buba.satiety >= 120:
#         print("Він луснув")
#         break

#     inp = input("Введіть функцію: ")
#     if inp == "how hungry?":
#         Buba.print_hungry()
#     elif inp == "working":
#         Buba.working()
#     elif inp == "do sport":
#         Buba.do_sport()
#     elif inp == "go dacia":
#         Buba.go_dacia()
#     elif inp == "info pizza":
#         pizza.print_saturation()
#     elif inp == "info buger":
#         buger.print_saturation()
#     elif inp == "info cockies":
#         cookies.print_saturation()
#     elif inp == "hungry?":
#         Buba.hungry()
#     elif inp == "eat pizza":
#          Buba.eating_pizza()
#     elif inp == "eat buger":
#         Buba.eating_buger()
#     elif inp == "eat cookies":
#         Buba.eating_cookies()
    