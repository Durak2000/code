import sqlite3

connection = sqlite3.connect('thebest.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

print('таблица create')

cursor.execute("INSERT INTO students (name, age) VALUES ('Alice', 52)")
cursor.execute("INSERT INTO students (name, age) VALUES ('Artur', 42)")
print('Данные вставлены')

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("Данные из таблицы 'student':")
for row in rows:
    print(row)

cursor.execute("UPDATE students SET age = 23 WHERE name = 'Artur'")
print('Данные обнавлены')

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("Данные из таблицы 'student':")
for row in rows:
    print(row)

cursor.execute("DELETE FROM students WHERE name = 'Alice'")
connection.commit()
print('Данные удалены')

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("Данные из таблицы 'student':")
for row in rows:
    print(row)

cursor.execute('ALTER TABLE students ADD COLUMN grade TEXT')
print("Структура таблицы 'students' изменена")

cursor.execute("CREATE INDEX idx_name ON students (name)")
print('Индекс "idx_name" создан')

cursor.execute('DROP INDEX idx_name')
print('Индекс "idx_name" удалён')

cursor.execute('DROP TABLE IF EXISTS students')
print('Таблица "students" удалена')

connection.close()
