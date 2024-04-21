# import sqlite3

# connection = sqlite3.connect("itstep_DB.sl3", 5)

# cur = connection.cursor()

# cur.execute("CREATE TABLE first_table (name TEXT);")


# print(connection)
# print(cur)
# connection.close()

#####################

# import sqlite3
 
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
 
# cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
# connection.commit()
 
# print(connection)
# print(cur)
# connection.close()

#############################

# import sqlite3
 
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
 
# cur.execute("SELECT rowid, name FROM first_table;")
# connection.commit()
 
# print(connection)
# print(cur)
# connection.close()

##############################

# import sqlite3
 
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
 
# cur.execute("SELECT rowid, name FROM first_table WHERE rowid=1;")
# connection.commit()
 
# print(connection)
# print(cur)
# connection.close()

##################################

# import sqlite3
 
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
 
# cur.execute("SELECT rowid, UPDATE first_table name='Kate' WHERE rowid=2;")
# connection.commit()
 
# print(connection)
# print(cur)
# connection.close()

#################################

# import sqlite3
 
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
 
# cur.execute("UPDATE first_table SET name='Kate' WHERE rowid=1;")
# connection.commit()
 
# print(connection)
# print(cur)
# connection.close()

############################

# import sqlite3
 
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
 
# cur.execute("DELETE FROM first_table WHERE rowid=1;")
# connection.commit()
 
# print(connection)
# print(cur)
# connection.close()

##################################

# import sqlite3
 
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
 
# cur.execute("DROP TABLE first_table;")
# connection.commit()
# connection.close()

####################################

# Імпортуємо модуль sqlite3
import sqlite3
 
# Встановлюємо з'єднання з базою даних SQLite
connection = sqlite3.connect("School.sl3")

# Створюємо об'єкт курсора
cur = connection.cursor()
 
# Виконуємо SQL-команду для створення таблиці Students
cur.execute('''CREATE TABLE IF NOT EXISTS Students
            (ID INTEGER PRIMARY KEY, Name TEXT, Age INTEGER)''')
 
# Виконуємо SQL-команду для створення таблиці Courses
cur.execute('''CREATE TABLE IF NOT EXISTS Courses
            (ID INTEGER PRIMARY KEY, Name TEXT, Teacher_ID INTEGER)''')
 
# Визначаємо дані для таблиці Students
students_data = [
    ('Alice', 20),
    ('Bob', 18),
    ('Max', 22),
    ('Dima', 15)
]
 
# Виконуємо SQL-команду для вставки даних в таблицю Students
cur.executemany("INSERT INTO Students (Name, Age) VALUES (?, ?)", students_data)
 
# Визначаємо дані для таблиці Courses
courses_data = [
    ('Math', 1),
    ('Physics', 2),
    ('Literature', 3)
]
 
# Виконуємо SQL-команду для вставки даних в таблицю Courses
cur.executemany("INSERT INTO Courses (Name, Teacher_ID) VALUES (?, ?)", courses_data)
 
# Здійснюємо зміни
connection.commit()

# Виконуємо SQL-команду для вибору студентів старше 18 років
cur.execute("SELECT * FROM Students WHERE AGE > 18")

# Друкуємо студентів старше 18 років
print("Студенти старші 18 років: ")
for row in cur.fetchall():
    print(row)

# Виконуємо SQL-команду для вибору студентів та їх курсів
cur.execute(''' SELECT Students.Name, Courses.Name FROM Students
            INNER JOIN Courses ON Students.ID = Courses.ID ''')

# Друкуємо студентів та їх курси
print("\nСписок студентів з назвами їх курсів: ")
for row in cur.fetchall():
    print(row)

# Закриваємо з'єднання з базою даних SQLite
connection.close()
