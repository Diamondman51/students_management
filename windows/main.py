from PySide6.QtWidgets import QApplication

from front_page import Window
from windows.login_dialog import Login

app = QApplication()

login = Login()
result = login.exec()
#
if result == Login.Accepted:
    window = Window()
    window.show()


# window.load_students()
if __name__ == '__main__':
    # window.show()
    app.exec()
