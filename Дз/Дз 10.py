# Завдання 1
# import sqlite3
# import random
# from datetime import datetime, timedelta

# # Підключитися до бази даних SQLite (або створити її)
# conn = sqlite3.connect('weather.db')

# # Створити об'єкт курсора
# c = conn.cursor()

# # Створити нову таблицю з двома полями: date_time та temperature
# c.execute('''
#     CREATE TABLE weather_data (
#         date_time TEXT,
#         temperature REAL
#     )
# ''')

# # Генеруємо рандомні дані для останніх 7 днів
# for i in range(7):
#     date_time = datetime.now() - timedelta(days=i)
#     temperature = random.uniform(-30, 30)  # Температура від -30 до 30 градусів

#     # Вставляємо дані в таблицю
#     c.execute("INSERT INTO weather_data (date_time, temperature) VALUES (?, ?)", (date_time, temperature))

# # Зберегти зміни та закрити з'єднання
# conn.commit()
# conn.close()
