from datetime import datetime

from random import randint

import psycopg2
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QDialog

from UI_files.studentDialog_UI import Ui_StudentsDialog


class StudentDialog(Ui_StudentsDialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# database_creation
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

        # Craete a cursor to execute PostgreSQL

        corsor = self.conn.cursor()

        # Create the database if it does not exist
        corsor.execute(f'Create database if not exists {database}')

        self.conn = psycopg2.connect(
            database=database,
            host=host,
            user=user,
            password=password,
            port=port
        )

        return self.conn


    # INSERT NEW STUDENT
    def insert_new_student(self):
        try:
            cursor = self.create_connection().cursor()
            gender = self.gender_comboBox.currentText()
            student_id = self.generate_studentId(gender)

            birthday = self.handleDateChange()

            # Assuming birthday is a QDate object
            birth_date = self.dob_dateEdit.date()
            age = self.calculate_age(birth_date)

            # Create list of student information

            self.new_student = [
                self.name_LineEdit.text(),
                student_id,
                self.gender_comboBox.currentText(),
                self.class_comboBox_2.currentText(),
                birthday,
                age,
                self.address_LineEdit.text(),
                self.phone_LineEdit.text(),
                self.email_LineEdit.text()
            ]

            # To put multiple rows in the PostgreSQL database

            insert_student_query = '''INSERT INTO students_table (names, student_id, gender, class, birthday, age, address, phone_number, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(insert_student_query, self.new_student)
            self.conn.commit()
            self.conn.close()

        except:
            pass


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
            cursor.execute(f'SELECT student_id FROM students_table WHERE student_id = %s, (student_id,)')
            existing_id = cursor.fetchone()
            if not existing_id:
                return student_id


    def generate_randomNumber(self):
        number = randint(1, 1000)
        random_number = f'{number:04d}'
        return random_number


    def handleDateChange(self):
        # convert QDate to a string in the format 'YYYY-MM-DD'
        selected_date = self.dob_dateEdit.date()
        self.date_string = selected_date.toString(Qt.ISODate)

        return self.date_string


    def calculate_age(self, bith_date):
        # get the current date
        current_date = datetime.now().date()

        # Create a date object for the birthdate
        bith_datetime = datetime(bith_date.year(), bith_date.month(), bith_date.day()).date()

        # Calculate the difference in years
        age = current_date.year - bith_datetime.year

        # Check if the current date has occured this year
        if (current_date.month, current_date.day) < (bith_datetime.month, bith_datetime.day):
            age -= 1

        return age