# class Studetnt:
#     print("Hi")
#     def __init__(self):
#         self.height = 160
#         print("I am alive!")
# first = Studetnt()

# class Student:
#     amount_of_student = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_student += 1
#
# nick = Student ()
# kate = Student (height=170)
# print(nick.amount_of_student)
# print(Student.amount_of_student)

# class Student:
#     height = 160
#     def __init__(self):
#         print(self.height)
#         self.height += 10
#
# nick = Student()
# kate = Student()

# class Miko:
#     strange = 9
#     live = 5400
#     damage = 1962

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_info(self):
#         return f"Im'я: {self.name}, Вік: {self.age}"
    
# student1 = Student("Іван", 2)
# print(student1.get_info())

import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    
    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
    
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
    
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
    
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()

nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
nick.live(day)