from PySide6.QtWidgets import QMainWindow

from ui_index import Ui_Form


class Window(Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)