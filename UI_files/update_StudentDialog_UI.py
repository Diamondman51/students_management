# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateStudentDialoggrcMGL.ui'
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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Update_StudentsDialog(object):
    def setupUi(self, Update_StudentsDialog):
        if not Update_StudentsDialog.objectName():
            Update_StudentsDialog.setObjectName(u"Update_StudentsDialog")
        Update_StudentsDialog.resize(548, 584)
        Update_StudentsDialog.setStyleSheet(u"QDialog {\n"
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
        self.line = QFrame(Update_StudentsDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 551, 31))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(Update_StudentsDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 411, 31))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(Update_StudentsDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 100, 511, 471))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.update_name_LineEdit = QLineEdit(self.layoutWidget)
        self.update_name_LineEdit.setObjectName(u"update_name_LineEdit")
        self.update_name_LineEdit.setMinimumSize(QSize(0, 35))
        self.update_name_LineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.update_name_LineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_6)

        self.update_gender_comboBox = QComboBox(self.layoutWidget)
        self.update_gender_comboBox.addItem("")
        self.update_gender_comboBox.addItem("")
        self.update_gender_comboBox.setObjectName(u"update_gender_comboBox")

        self.verticalLayout_5.addWidget(self.update_gender_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.update_class_comboBox_2 = QComboBox(self.layoutWidget)
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.addItem("")
        self.update_class_comboBox_2.setObjectName(u"update_class_comboBox_2")

        self.verticalLayout_6.addWidget(self.update_class_comboBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.update_dob_dateEdit = QDateEdit(self.layoutWidget)
        self.update_dob_dateEdit.setObjectName(u"update_dob_dateEdit")
        self.update_dob_dateEdit.setCalendarPopup(True)

        self.verticalLayout_7.addWidget(self.update_dob_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.update_address_LineEdit = QLineEdit(self.layoutWidget)
        self.update_address_LineEdit.setObjectName(u"update_address_LineEdit")
        self.update_address_LineEdit.setMinimumSize(QSize(0, 35))
        self.update_address_LineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.update_address_LineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.update_phone_LineEdit = QLineEdit(self.layoutWidget)
        self.update_phone_LineEdit.setObjectName(u"update_phone_LineEdit")
        self.update_phone_LineEdit.setMinimumSize(QSize(0, 35))
        self.update_phone_LineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.update_phone_LineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.update_email_LineEdit = QLineEdit(self.layoutWidget)
        self.update_email_LineEdit.setObjectName(u"update_email_LineEdit")
        self.update_email_LineEdit.setMinimumSize(QSize(0, 35))
        self.update_email_LineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.update_email_LineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.update_saveStudent_btn = QPushButton(self.layoutWidget)
        self.update_saveStudent_btn.setObjectName(u"update_saveStudent_btn")
        self.update_saveStudent_btn.setMinimumSize(QSize(120, 41))
        self.update_saveStudent_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:#34D481;\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 8;\n"
"	font-weight: bold;\n"
"	font-size:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.update_saveStudent_btn)

        self.update_cancel_btn = QPushButton(self.layoutWidget)
        self.update_cancel_btn.setObjectName(u"update_cancel_btn")
        self.update_cancel_btn.setMinimumSize(QSize(120, 41))
        self.update_cancel_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:#585858;\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 8;\n"
"	font-weight: bold;\n"
"	font-size:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.update_cancel_btn)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)


        self.retranslateUi(Update_StudentsDialog)

        QMetaObject.connectSlotsByName(Update_StudentsDialog)
    # setupUi

    def retranslateUi(self, Update_StudentsDialog):
        Update_StudentsDialog.setWindowTitle(QCoreApplication.translate("Update_StudentsDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Update_StudentsDialog", u"Update Student Information", None))
        self.label_2.setText(QCoreApplication.translate("Update_StudentsDialog", u"Full Name", None))
        self.label_6.setText(QCoreApplication.translate("Update_StudentsDialog", u"Select Gendet", None))
        self.update_gender_comboBox.setItemText(0, QCoreApplication.translate("Update_StudentsDialog", u"Male", None))
        self.update_gender_comboBox.setItemText(1, QCoreApplication.translate("Update_StudentsDialog", u"Female", None))

        self.label_7.setText(QCoreApplication.translate("Update_StudentsDialog", u"Select Class", None))
        self.update_class_comboBox_2.setItemText(0, QCoreApplication.translate("Update_StudentsDialog", u"Grade 1", None))
        self.update_class_comboBox_2.setItemText(1, QCoreApplication.translate("Update_StudentsDialog", u"Grade 2", None))
        self.update_class_comboBox_2.setItemText(2, QCoreApplication.translate("Update_StudentsDialog", u"Grade 3", None))
        self.update_class_comboBox_2.setItemText(3, QCoreApplication.translate("Update_StudentsDialog", u"Grade 4", None))
        self.update_class_comboBox_2.setItemText(4, QCoreApplication.translate("Update_StudentsDialog", u"Grade 5", None))
        self.update_class_comboBox_2.setItemText(5, QCoreApplication.translate("Update_StudentsDialog", u"Grade 6", None))
        self.update_class_comboBox_2.setItemText(6, QCoreApplication.translate("Update_StudentsDialog", u"Grade 7", None))
        self.update_class_comboBox_2.setItemText(7, QCoreApplication.translate("Update_StudentsDialog", u"Grade 8", None))
        self.update_class_comboBox_2.setItemText(8, QCoreApplication.translate("Update_StudentsDialog", u"Grade 9", None))
        self.update_class_comboBox_2.setItemText(9, QCoreApplication.translate("Update_StudentsDialog", u"Grade 10", None))
        self.update_class_comboBox_2.setItemText(10, QCoreApplication.translate("Update_StudentsDialog", u"Grade 11", None))

        self.label_8.setText(QCoreApplication.translate("Update_StudentsDialog", u"Date of Birth", None))
        self.update_dob_dateEdit.setDisplayFormat(QCoreApplication.translate("Update_StudentsDialog", u"dd/MM/yyyy", None))
        self.label_3.setText(QCoreApplication.translate("Update_StudentsDialog", u"Address", None))
        self.label_4.setText(QCoreApplication.translate("Update_StudentsDialog", u"Phone Number", None))
        self.label_5.setText(QCoreApplication.translate("Update_StudentsDialog", u"Email", None))
        self.update_saveStudent_btn.setText(QCoreApplication.translate("Update_StudentsDialog", u"Update Student", None))
        self.update_cancel_btn.setText(QCoreApplication.translate("Update_StudentsDialog", u"Cancel", None))
    # retranslateUi

