from PySide6.QtWidgets import QApplication

from front_page import Window

app = QApplication()

window = Window()
if __name__ == '__main__':
    window.show()
    app.exec()
