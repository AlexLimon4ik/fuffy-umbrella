import sqlite3
connection = sqlite3.connect("itstep_DB.sl3", 5)
cur =connection.cursor()

cur.execute("CREATE TABLE first_table (name TEXT);")

print(connection)
print(cur)
connection.close