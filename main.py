# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3
from PyQt5 import QtSql

# Создаем соединение с нашей базой данных
conn = sqlite3.connect('db.sqlite3')
# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()
# Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
cursor.execute("SELECT nregion FROM main_region ORDER BY nregion LIMIT 3")
# Получаем результат сделанного запроса
results = cursor.fetchall()

print(results)

#Не забываем закрыть соединение с базой данных
conn.close()


class SQL_TEST():

    pass




