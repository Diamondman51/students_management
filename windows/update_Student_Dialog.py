from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog

from UI_files.update_StudentDialog_UI import Ui_Update_StudentsDialog


class Update_studentDialog(Ui_Update_StudentsDialog, QDialog):
    def __init__(self, row_index, row_data):
        super().__init__()
        self.setupUi(self)
        self.row_index = row_index
        self.row_data = row_data
        self.setWindowTitle('Update Student Dialog')
        self.setWindowIcon(QIcon('../resources/images/logo (1).png'))
