import sys
import sqlite3
import pyodbc


# подключение к MSSQL
server = 'BUDA\SQLEXPRESS'
database = 'LISTIM2015'
username = 'sa'
password = 'IwB1966Y'
con_str = 'DRIVER={SQL Server Native Client 11.0}; SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + \
          ';PWD=' + password
cnxn = pyodbc.connect(con_str)
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM RDList')
# rows = cursor.fetchall()
# for row in rows:
#     print(row.naim)

# row = cursor.fetchone()
# print(row[i] for i in enumerate(row))

# Подключение к SQLite
# Создаем соединение с нашей базой данных
conn = sqlite3.connect('db.sqlite3')
# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor2 = conn.cursor()
# Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
# cursor.execute("SELECT nregion FROM main_region ORDER BY nregion LIMIT 3")
cursor2.execute(
    ''' CREATE TABLE IF NOT EXISTS RDListIO
    (
         naim text, 
         prot FLOAT,
         invnum text,
         idnum text,
         bals FLOAT,
         osts FLOAT,
         cod text,
         amgroup NUMERIC,
         norma NUMERIC,
         byear NUMERIC,
         pikets text,
         most1 FLOAT, am1 FLOAT, most2 FLOAT, am2 FLOAT, most3 FLOAT, am3 FLOAT, most4 FLOAT, am4 FLOAT,
         most5 FLOAT, am5 FLOAT, most6 FLOAT, am6 FLOAT, most7 FLOAT, am7 FLOAT, most8 FLOAT, am8 FLOAT,
         most9 FLOAT, am9 FLOAT, most10 FLOAT, am10 FLOAT, most11 FLOAT, am11 FLOAT, most12 FLOAT, am12 FLOAT,
         most13 FLOAT, am13 FLOAT
    )
    '''
               )

rows = cursor.fetchall()
strsql = 'INSERT INTO RDList VALUES(' + ','.join(['?' for _ in range(37)])+')'
cursor2.executemany(strsql,([[(row[i]) for i in range(37)] for row in rows]))

conn.commit()
#     pass


# Получаем результат сделанного запроса
#(results,) = cursor.fetchone()
#print(type(results))
# Не забываем закрыть соединение с базой данных
conn.close()
