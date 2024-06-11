from datetime import datetime
from random import randint

import psycopg2
from PySide6.QtCore import QDate, Signal
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QDialog, QMessageBox

from UI_files.update_StudentDialog_UI import Ui_Update_StudentsDialog


class Update_studentDialog(Ui_Update_StudentsDialog, QDialog):

    data_updated = Signal()

    def __init__(self, row_index, row_data):
        super().__init__()
        self.setupUi(self)
        self.row_index = row_index
        self.row_data = row_data
        self.setWindowTitle('Update Student Dialog')
        self.setWindowIcon(QIcon('../resources/images/logo (1).png'))

        self.student_info = self.select_student()[0]

        self.student_name_info = self.student_info[0]
        self.student_id_info = self.student_info[1]
        self.student_gender_info = self.student_info[2]
        self.student_grade_info = self.student_info[3]
        self.student_birthday_info = self.student_info[4]
        self.student_age_info = self.student_info[5]
        self.student_address_info = self.student_info[6]
        self.student_phone_info = self.student_info[7]
        self.student_email_info = self.student_info[8]


        # For the Date from PostgreSQL Database, first convert string to a QDate before displaying it in the QDateEtid
        date_object = QDate.fromString(self.student_birthday_info, 'yyyy-MM-dd')

        self.update_name_LineEdit.setText(self.student_name_info)
        self.update_gender_comboBox.setCurrentText(self.student_gender_info)
        self.update_class_comboBox_2.setCurrentText(self.student_grade_info)
        self.update_dob_dateEdit.setDate(date_object)
        self.update_address_LineEdit.setText(self.student_address_info)
        self.update_phone_LineEdit.setText(self.student_phone_info)
        self.update_email_LineEdit.setText(self.student_email_info)

        self.lastIndex = self.update_gender_comboBox.currentText()
        self.update_saveStudent_btn.clicked.connect(self.update_data)
        self.update_cancel_btn.clicked.connect(self.close)

        # print(self.student_info)
        # print('row_data:', row_data)

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

    def select_student(self):

        self.cursor = self.create_connection().cursor()

        # Get students varuables from the tuple
        self.student_name = self.row_data[0]
        self.student_id = self.row_data[1]

        params = [
            self.student_name,
            self.student_id
        ]

        query = f'''select * from students_table where (names=%s and student_id=%s)'''

        self.cursor.execute(query, params)

        records = self.cursor.fetchall()

        self.conn.commit()
        self.conn.close()

        return records

    def update_data(self):

        try:
            connection = self.create_connection()
            if connection is None:
                return

            cursor = connection.cursor()

            # Assuming birthdate is a QDateobject
            birth_date = self.update_dob_dateEdit.date()
            birthday = self.handleDateChange()
            age = self.calculate_age(birth_date)

            # Check if the student gender changed. We create a new student id in this case
            current_student_id = self.on_gender_change(self.update_gender_comboBox.currentText())

            params = (
                self.update_name_LineEdit.text(),
                current_student_id,
                self.update_gender_comboBox.currentText(),
                self.update_class_comboBox_2.currentText(),
                birthday,
                age,
                self.update_address_LineEdit.text(),
                self.update_phone_LineEdit.text(),
                self.update_email_LineEdit.text(),
                self.student_id_info
            )

            print(params)

            update_query = f'''update students_table set names=%s, student_id=%s, gender=%s, class=%s, birthday=%s, age=%s, address=%s, phone_number=%s, email=%s where student_id=%s'''

            cursor.execute(update_query, params)
            connection.commit()
            self.show_updated_message()
            connection.close()
            self.close()

            self.data_updated.emit()

        except psycopg2.errors.SyntaxError as error:
            print('Error:', error)


    def handleDateChange(self):
        # convert QDate to a string in the format 'YYYY-MM-DD'
        selected_date = self.update_dob_dateEdit.date()
        self.date_string = selected_date.toString(Qt.ISODate)

        return self.date_string


    def calculate_age(self, bith_date):
        # get the current date
        current_date = datetime.now().date()

        # Create a date object for the birthdate
        birth_datetime = datetime(bith_date.year(), bith_date.month(), bith_date.day()).date()

        # Calculate the difference in years
        age = current_date.year - birth_datetime.year

        # Check if the current date has occured this year
        if (current_date.month, current_date.day) < (birth_datetime.month, birth_datetime.day):
            age -= 1

        return age

    def on_gender_change(self, index):

        if index != self.lastIndex:

            gender_item = self.update_gender_comboBox.currentText()
            new_student_id = self.generate_studentId(gender_item)

            return new_student_id

        else:
            return self.student_id_info

    def generate_studentId(self, gender):
        cursor = self.create_connection().cursor()

        while True:
            if gender == 'Male':
                id_start_value = '24' + '/U/M'
            else:
                id_start_value = '24' + '/U/F'

            random_value = self.generate_randomNumber()
            student_id = id_start_value + random_value

            # check if the generated student id is already in the table
            cursor.execute(f'SELECT student_id FROM students_table WHERE student_id = %s', (student_id,))
            # cursor.close()
            existing_id = cursor.fetchone()
            if not existing_id:
                return student_id


    def generate_randomNumber(self):
        number = randint(1, 1000)
        random_number = f'{number:04d}'
        return random_number

    def show_updated_message(self):
        msg_Box = QMessageBox(self)
        msg_Box.setWindowTitle('Success')
        msg_Box.setText(self.student_name_info + "'s" + ' Information successfully changed to ' + self.update_name_LineEdit.text())
        msg_Box.exec()

