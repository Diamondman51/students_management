from PySide6.QtWidgets import QApplication

from front_page import Window

app = QApplication()

mainWindow = Window()
mainWindow.show()
app.exec()