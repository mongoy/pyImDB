# Импортируем библиотеку, соответствующую типу нашей базы данных
import sys
import sqlite3
from PyQt5 import QtSql
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QIcon,QFont


class MainW(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setGeometry(400, 400, 1000, 220)
        self.setWindowTitle('Перечень автомобильных дорог')
        self.setWindowIcon(QIcon('web.png'))
        self.show()


    def stat_db(self):

        # Создаем соединение с нашей базой данных
        conn = sqlite3.connect('db.sqlite3')
        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        cursor = conn.cursor()
        # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
        cursor.execute("SELECT nregion FROM main_region ORDER BY nregion LIMIT 3")
        # Получаем результат сделанного запроса
        results = cursor.fetchall()

        #print(results)

        # Не забываем закрыть соединение с базой данных
        conn.close()

    print(stat_db())


# точка входа
if __name__ == '__main__':

    # Создание окна Запускается основной цикл
    app = QApplication(sys.argv)  # приложение
    mainw = MainW()
    sys.exit(app.exec_()) # главный виджет уничтожен





