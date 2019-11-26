# Импортируем библиотеку, соответствующую типу нашей базы данных
import sys
import sqlite3
import pyodbc
from PyQt5 import QtSql, uic, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.uic.properties import QtGui
from main_window import Ui_MainWindow


class MainW(QtWidgets.QMainWindow):
    q_road = ("SELECT count(DISTINCT nroad) as croad FROM main_road",\
              "SELECT sum(lroad) AS sroad FROM main_road")

    def __init__(self):
        super(MainW, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setText("Всего дорог: " + str(self.stat_db(self.q_road[0])))
        #self.ui.label_2.setText("Протяженность (км): " + str(self.stat_db(self.q_road[1])))
        #self.ui.label_2.setText("Протяженность (км): " + str(self.stat_mssql(self)))

    def stat_db(self,y):
        # Создаем соединение с нашей базой данных
        conn = sqlite3.connect('db.sqlite3')
        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        cursor = conn.cursor()
        # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
        # cursor.execute("SELECT nregion FROM main_region ORDER BY nregion LIMIT 3")
        cursor.execute(str(y))
        # Получаем результат сделанного запроса
        (results,) = cursor.fetchone()
        print(type(results))
        # Не забываем закрыть соединение с базой данных
        conn.close()
        return results

    def stat_mssql(self):
        # Some other example server values are
        # server = 'localhost\sqlexpress' # for a named instance
        # server = 'myserver,port' # to specify an alternate port
        server = 'tcp:buda'
        database = 'LISTIM2015'
        username = 'GKU/aantropov'
        password = 'P2473Wl'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        print('sql')
        return 0




# # print(stat_db())


# точка входа
if __name__ == '__main__':
    # Создание окна Запускается основной цикл
    app = QtWidgets.QApplication(sys.argv)
    application = MainW()
    application.show()
    sys.exit(app.exec_())  # главный виджет уничтожен
