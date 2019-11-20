# Импортируем библиотеку, соответствующую типу нашей базы данных
import sys
import sqlite3
from PyQt5 import QtSql, uic, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from main_window import Ui_MainWindow


class MainW(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainW,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

# def stat_db(self):
#     # Создаем соединение с нашей базой данных
#     conn = sqlite3.connect('db.sqlite3')
#     # Создаем курсор - это специальный объект который делает запросы и получает их результаты
#     cursor = conn.cursor()
#     # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
#     cursor.execute("SELECT nregion FROM main_region ORDER BY nregion LIMIT 3")
#     # Получаем результат сделанного запроса
#     results = cursor.fetchall()
#
#     # print(results)
#
#     # Не забываем закрыть соединение с базой данных
#     conn.close()
#
# # print(stat_db())


# точка входа
if __name__ == '__main__':
    # Создание окна Запускается основной цикл
    app = QtWidgets.QApplication([])
    application = MainW()
    application.show()
    sys.exit(app.exec_())  # главный виджет уничтожен
