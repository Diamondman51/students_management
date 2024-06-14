from PySide6.QtWidgets import QWidget, QApplication

from ui_files.ui_Button_tools import Ui_Form


class Button_tools(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.setFixedWidth(500)
        # self.setFixedHeight(50)


# app = QApplication()
# window = Button_tools()
# window.show()
# app.exec()