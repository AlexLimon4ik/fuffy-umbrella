class NoInList(Exception):
    def __str__(self):
        return "В списку немає такої людини"

class People:
    def __init__(self, name="", age=0):
        self.name = name 
        self.age = age
        self.category = self.get_category()

    def get_category(self):
        if self.age < 18:
            return "Child"
        elif 18 <= self.age < 50:
            return "Adult"
        elif 50 <= self.age <= 65:
            return "Aged"
        elif 65 < self.age < 90:
            return "Old"
        elif 90 <= self.age:
            return "Very old"

Sasha = People("Sasha", 12)
Katya = People("Katya", 35)
Nadya = People("Nadya", 56)
Vova = People("Vova", 71)
Masha = People("Masha", 89)

livers = [Sasha, Katya, Nadya, Vova, Masha]

inp = str(input("Введіть ваше ім'я: "))

for person in livers:
    if person.name == inp:
        print(f"{inp} належить до групи '{person.category}'")
        break
else:
    raise NoInList()
