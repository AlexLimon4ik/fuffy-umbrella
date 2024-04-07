import colorama

all_attributes_and_methods = dir(colorama)

print("Всі атрибути та методи(В стопчик): ")
for item in all_attributes_and_methods:
    print(item)
print("init(autoreset=False, strip=None, wrap=True, convert=None, **kwargs): цей метод \
іціалізує бібліотеку та налаштовує параметри виведення кольорового тексту в консоль")
print("Fore: цей клас містить атрибути, які дозволяють задавати кольорові налаштування для переднього плану тексту")
print("Back: цей клас містить атрибути, які дозволяють задавати кольорові налаштування для заднього плану тексту")
print("Style: цей клас містить атрибути, які дозволяють задавати стиль тексту (жирний, курсивний тощо)")
