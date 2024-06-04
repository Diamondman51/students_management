# -*- coding: utf-8 -*-
from random import randint

################################################################################
## Form generated from reading UI file 'studentDialogMseLhQ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import sqlite3
class Ui_StudentsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(548, 584)
        self.setStyleSheet(u"QDialog {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid grey;\n"
"	border-radius: 6;\n"
"	padding-left: 15px;\n"
"	height: 35;\n"
"}\n"
"\n"
"QDateEdit {\n"
"	border: 1px solid grey;\n"
"	border-radius: 6;\n"
"	padding-left: 15px;\n"
"	height: 31;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border: 1px solid white;\n"
"	border-radius: 8;\n"
"	padding: 1 18 1 15;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	height: 35;\n"
"	font-weight: bold;\n"
"	selection-background-color: #2980B9\n"
"}")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 551, 31))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 281, 31))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 100, 511, 401))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name_LineEdit = QLabel(self.layoutWidget)
        self.name_LineEdit.setObjectName(u"name_LineEdit")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.name_LineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.name_LineEdit)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 35))
        self.lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_6)

        self.gender_comboBox = QComboBox(self.layoutWidget)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")

        self.verticalLayout_5.addWidget(self.gender_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.class_comboBox_2 = QComboBox(self.layoutWidget)
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.setObjectName(u"class_comboBox_2")

        self.verticalLayout_6.addWidget(self.class_comboBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.dob_dateEdit = QDateEdit(self.layoutWidget)
        self.dob_dateEdit.setObjectName(u"dob_dateEdit")

        self.verticalLayout_7.addWidget(self.dob_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.address_LineEdit = QLabel(self.layoutWidget)
        self.address_LineEdit.setObjectName(u"address_LineEdit")
        self.address_LineEdit.setFont(font1)

        self.verticalLayout_2.addWidget(self.address_LineEdit)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 35))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.phone_LineEdit = QLabel(self.layoutWidget)
        self.phone_LineEdit.setObjectName(u"phone_LineEdit")
        self.phone_LineEdit.setFont(font1)

        self.verticalLayout_3.addWidget(self.phone_LineEdit)

        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 35))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.email_LineEdit = QLabel(self.layoutWidget)
        self.email_LineEdit.setObjectName(u"email_LineEdit")
        self.email_LineEdit.setFont(font1)

        self.verticalLayout_4.addWidget(self.email_LineEdit)

        self.lineEdit_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 35))
        self.lineEdit_4.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(300, 520, 231, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.saveStudent_btn = QPushButton(self.layoutWidget1)
        self.saveStudent_btn.setObjectName(u"saveStudent_btn")
        self.saveStudent_btn.setMinimumSize(QSize(111, 41))
        self.saveStudent_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:#34D481;\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 8;\n"
"	font-weight: bold;\n"
"	font-size:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.saveStudent_btn)

        self.cancel_btn = QPushButton(self.layoutWidget1)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(75, 41))
        self.cancel_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:#585858;\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 8;\n"
"	font-weight: bold;\n"
"	font-size:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.cancel_btn)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, StudentsDialog):
        StudentsDialog.setWindowTitle(QCoreApplication.translate("StudentsDialog", u"Student Dialog", None))
        self.label.setText(QCoreApplication.translate("StudentsDialog", u"Add New Student", None))
        self.name_LineEdit.setText(QCoreApplication.translate("StudentsDialog", u"Full Name", None))
        self.label_6.setText(QCoreApplication.translate("StudentsDialog", u"Select Gendet", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Male", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Female", None))

        self.label_7.setText(QCoreApplication.translate("StudentsDialog", u"Select Class", None))
        self.class_comboBox_2.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Grade 1", None))
        self.class_comboBox_2.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Grade 2", None))
        self.class_comboBox_2.setItemText(2, QCoreApplication.translate("StudentsDialog", u"Grade 3", None))
        self.class_comboBox_2.setItemText(3, QCoreApplication.translate("StudentsDialog", u"Grade 4", None))
        self.class_comboBox_2.setItemText(4, QCoreApplication.translate("StudentsDialog", u"Grade 5", None))
        self.class_comboBox_2.setItemText(5, QCoreApplication.translate("StudentsDialog", u"Grade 6", None))
        self.class_comboBox_2.setItemText(6, QCoreApplication.translate("StudentsDialog", u"Grade 7", None))
        self.class_comboBox_2.setItemText(7, QCoreApplication.translate("StudentsDialog", u"Grade 8", None))
        self.class_comboBox_2.setItemText(8, QCoreApplication.translate("StudentsDialog", u"Grade 9", None))
        self.class_comboBox_2.setItemText(9, QCoreApplication.translate("StudentsDialog", u"Grade 10", None))
        self.class_comboBox_2.setItemText(10, QCoreApplication.translate("StudentsDialog", u"Grade 11", None))

        self.label_8.setText(QCoreApplication.translate("StudentsDialog", u"Date of Birth", None))
        self.address_LineEdit.setText(QCoreApplication.translate("StudentsDialog", u"Address", None))
        self.phone_LineEdit.setText(QCoreApplication.translate("StudentsDialog", u"Phone Number", None))
        self.email_LineEdit.setText(QCoreApplication.translate("StudentsDialog", u"Email", None))
        self.saveStudent_btn.setText(QCoreApplication.translate("StudentsDialog", u"Add Student", None))
        self.cancel_btn.setText(QCoreApplication.translate("StudentsDialog", u"Cancel", None))
    # retranslateUi


    # database_creation
    def create_connection(self):
        database_name = 'my_school.db'
        with sqlite3.connect(database_name) as database:
            create_students_table_query = """
            CREATE TABLE IF NOT EXISTS students_table(
            names TEXT,
            student_id VARCHAR(15) PRIMARY KEY,
            gender TEXT,
            class TEXT,
            birthday TEXT,
            age INT,
            address TEXT,
            phone_number VARCHAR(15),
            email VARCHAR(15)
            );
            """
            database.execute(create_students_table_query)
# INSERT NEW STUDENT
    def insert_new_student(self):
        try:
            gender = self.gender_comboBox.currentText()
            student_id = self.generate_studentId(gender)

        except:
            pass

    def generate_studentId(self, gender):
        database_name = 'my_school.db'
        with sqlite3.connect(database_name) as database:


            while True:
                if gender == 'Male':
                    id_start_value = '24' + '/U/M'
                else:
                    id_start_value = '24' + '/U/F'

                random_value = self.generate_randomNumber()
                student_id = id_start_value + random_value

                # check if the generated student id is already in the table
                database.execute(f'SELECT student_id FROM students_table WHERE student_id = %s, (student_id,)')
                # existing_id = database


    def generate_randomNumber(self):

        number = randint(1, 1000)
        random_number = f'{number:04d}'
        return random_number