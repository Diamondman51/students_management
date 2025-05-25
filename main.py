
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
import sys
from PySide6.QtWidgets import QApplication


from windows.front_page import Window
from windows.login_dialog import Login

app = QApplication(sys.argv)
app.setStyle('Fusion')

# login = Login()
# result = login.exec()
#
# if result == Login.Accepted:
    
window = Window()
window.show()
# elif not result:
#     sys.exit()

# window.load_students()
if __name__ == '__main__':
    # window.show()
    app.exec()





