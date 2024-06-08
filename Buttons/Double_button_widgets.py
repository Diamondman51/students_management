from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton

from windows.update_Student_Dialog import Update_studentDialog


# Create double button class
class DoubleButtonWidgetStudents(QWidget):
    def __init__(self, row_index, row_data):
        super().__init__()

        # store the row index and row data as an instance in variables
        self.row_index = row_index
        self.row_data = row_data

        # Get student varuables from the tuple
        self.student_name = self.row_data[0]
        self.student_id = self.row_data[1]

        layout = QHBoxLayout(self)

        # Create Blue Edit button
        self.edit_button = QPushButton(self)
        # self.edit_button.setFixedSize(QSize(20, 20))
        self.edit_button.setStyleSheet('''
                                        background-color:blue; 
                                        padding:0;
                                        ''')
        self.edit_button.setFixedSize(61, 31)

        # Create Red Delete button
        self.delete_button = QPushButton(self)
        # self.delete_button.setFixedSize(QSize(20, 20))
        self.delete_button.setStyleSheet(''' 
                                        background-color:red; 
                                        padding:0;
                                        ''')
        self.delete_button.setFixedSize(61, 31)

        # Set Icons for the buttons
        icon = QIcon(r'../resources/images/edit.png')
        self.edit_button.setIcon(icon)

        icon2 = QIcon('../resources/images/delete.png')
        self.delete_button.setIcon(icon2)

        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        self.setLayout(layout)

    def edit_clicked(self):
        # Create an instance of UpdateStudent Dialog
        self.update_dialog = Update_studentDialog(self.row_index, self.row_data)

        # Execute the update dialog
        self.update_dialog.exec()

    def delete_clicked(self):
        pass