from PySide6.QtWidgets import QWidget, QApplication
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import sys
sys.path.append(str(BASE_DIR))

from ui_files.ui_Button_tools import Ui_Form


class Button_tools(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# app = QApplication()
# window = Button_tools()
# window.show()
# app.exec()