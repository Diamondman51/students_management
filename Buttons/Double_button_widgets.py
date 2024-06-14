import psycopg2
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QMessageBox

from windows.update_Student_Dialog import Update_studentDialog


# Create double button class
class DoubleButtonWidgetStudents(QWidget):

    instance = None

    def __init__(self, row_index, row_data, SideBar):
        super().__init__()

        # store the row index and row data as an instance in variables
        self.row_index = row_index
        self.row_data = row_data
        self.side_bar = SideBar # Store a reference to MySideBar

        # Get student variables from the tuple
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
        self.edit_button.clicked.connect(self.edit_clicked)

        # Create Red Delete button
        self.delete_button = QPushButton(self)
        # self.delete_button.setFixedSize(QSize(20, 20))
        self.delete_button.setStyleSheet(''' 
                                        background-color:red; 
                                        padding:0;
                                        ''')
        self.delete_button.setFixedSize(61, 31)
        self.delete_button.clicked.connect(self.delete_clicked)

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

        # Connect the custom signal to reload_Students_data slot in MySideBar
        self.update_dialog.data_updated.connect(self.side_bar.reloadStudentstable_data)


        # Execute the update dialog
        self.update_dialog.exec()

    def create_connection(self):
        # Establish connection
        database = 'school management'
        host = 'localhost'
        user = 'postgres'
        password = 'Zshavkatov61@'
        port = '5432'

        self.conn = psycopg2.connect(
            database=database,
            host=host,
            user=user,
            password=password,
            port=port
        )

        return self.conn

    def delete_clicked(self):

        cursor = self.create_connection().cursor()

        # Create a confirmation message dialog
        messsage = QMessageBox.question(
            self, 'Confirmation',
            'Are you sure you want to delete ' + self.student_name + ' ?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if messsage == QMessageBox.StandardButton.Yes:
            # Delete the row from students table

            delete_query = f'''delete from students_table where student_id=%s'''

            cursor.execute(delete_query, (self.student_id,))
            self.conn.commit()
            self.conn.close()

            # Emit a signal to inform about data change
            self.side_bar.reloadStudentstable_data()

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls(0, ('Java', '24/U/M0690', 'Male', 'Grade 1', '2000-01-01', 24, 'fsefsfezbtdrtbebdrtbdihusuiweuinecnesnwcknjfolsolikvdmnsefnklkjnsjkdxvbjmn cxvmn cx', '894131213', 'dadawdsefgrdsgdrgdrgd'))
        return
