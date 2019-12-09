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
    # q_road = ("SELECT count(DISTINCT nroad) as croad FROM main_road",\
    #           "SELECT sum(lroad) AS sroad FROM main_road")

    q_road = ("SELECT count(DISTINCT naim) as croad FROM RDList",\
              "SELECT SUM(prot) AS sroad, SUM(bals) AS sum_bal, SUM(osts) AS sum_ost FROM RDList")

    def __init__(self):
        super(MainW, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setText("Всего дорог: " + str(self.db_sqlite(self.q_road[0])))
        self.ui.label_2.setText("Протяженность (км): " + str(self.db_sqlite(self.q_road[0])))

    def db_sqlite(self, y):
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

    def db_mssql(self, y):
        # Some other example server values are
        # server = 'localhost\sqlexpress' # for a named instance
        # server = 'myserver,port' # to specify an alternate port
        server = 'BUDA\SQLEXPRESS'
        database = 'LISTIM2015'
        username = 'sa'
        password = 'IwB1966Y'
        con_str = 'DRIVER={SQL Server Native Client 11.0}; SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
        cnxn = pyodbc.connect(con_str)
        cursor = cnxn.cursor()
        #cursor.execute(str(y))
        #print('sql')
        return 0




#print(stat_mssql())


# точка входа
if __name__ == '__main__':
    # Создание окна Запускается основной цикл
    app = QtWidgets.QApplication(sys.argv)
    application = MainW()
    application.show()
    sys.exit(app.exec_())  # главный виджет уничтожен
