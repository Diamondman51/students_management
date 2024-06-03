from PySide6.QtWidgets import QApplication

from front_page import MySideBar

app = QApplication()

mainWindow = MySideBar()

if __name__ == '__main__':
    mainWindow.show()
    app.exec()
