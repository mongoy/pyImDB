# Импортируем библиотеку, соответствующую типу нашей базы данных
import sys
import sqlite3
from PyQt5 import QtSql, uic, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.uic.properties import QtGui
from main_window import Ui_MainWindow


class MainW(QtWidgets.QMainWindow):
    q_road = ("SELECT count(DISTINCT nroad) as croad FROM main_road",\
              "SELECT count(DISTINCT nroad) as croad FROM main_road")

    def __init__(self):
        super(MainW, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        for x in enumerate(self.q_road):
            self.ui.label.setText("Всего дорог:" + str(self.stat_db(self.q_road[0])))
        #a = self.stat_db()
        #print(a)
        # print(str([i[0] for i in self.stat_db()]))

    def stat_db(self,y):
        # Создаем соединение с нашей базой данных
        conn = sqlite3.connect('db.sqlite3')
        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        cursor = conn.cursor()
        # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
        # cursor.execute("SELECT nregion FROM main_region ORDER BY nregion LIMIT 3")
        cursor.execute(str(y))
        # Получаем результат сделанного запроса
        results = cursor.fetchall()

        # Не забываем закрыть соединение с базой данных
        conn.close()
        return results


# # print(stat_db())


# точка входа
if __name__ == '__main__':
    # Создание окна Запускается основной цикл
    app = QtWidgets.QApplication(sys.argv)
    application = MainW()
    application.show()
    sys.exit(app.exec_())  # главный виджет уничтожен
