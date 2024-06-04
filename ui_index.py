# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indexGnHLHZ.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1231, 880)
        Form.setMinimumSize(QSize(1231, 880))
        Form.setMaximumSize(QSize(12333, 880))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(3, -5, 1233, 881))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.layoutWidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(71, 0))
        self.icon_only_widget.setMaximumSize(QSize(71, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-radius: 3px;\n"
"}\n"
"")
        self.verticalLayout_12 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/images/logo (1).png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/images/dashboardsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/dashboardsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.dashboard_1)

        self.institution_1 = QPushButton(self.icon_only_widget)
        self.institution_1.setObjectName(u"institution_1")
        icon1 = QIcon()
        icon1.addFile(u":/images/institutionsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/institutionsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.institution_1.setIcon(icon1)
        self.institution_1.setIconSize(QSize(100, 16))
        self.institution_1.setCheckable(True)
        self.institution_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.institution_1)

        self.students_1 = QPushButton(self.icon_only_widget)
        self.students_1.setObjectName(u"students_1")
        icon2 = QIcon()
        icon2.addFile(u":/images/studentssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/studentssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.students_1.setIcon(icon2)
        self.students_1.setIconSize(QSize(100, 20))
        self.students_1.setCheckable(True)
        self.students_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.students_1)

        self.teachers_1 = QPushButton(self.icon_only_widget)
        self.teachers_1.setObjectName(u"teachers_1")
        icon3 = QIcon()
        icon3.addFile(u":/images/teacherssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/teacherssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.teachers_1.setIcon(icon3)
        self.teachers_1.setIconSize(QSize(100, 20))
        self.teachers_1.setCheckable(True)
        self.teachers_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.teachers_1)

        self.finance_1 = QPushButton(self.icon_only_widget)
        self.finance_1.setObjectName(u"finance_1")
        icon4 = QIcon()
        icon4.addFile(u":/images/financessmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/financessmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.finance_1.setIcon(icon4)
        self.finance_1.setIconSize(QSize(100, 20))
        self.finance_1.setCheckable(True)
        self.finance_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.finance_1)


        self.verticalLayout_12.addLayout(self.verticalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 455, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        icon5 = QIcon()
        icon5.addFile(u":/images/settingssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/images/settingssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_1.setIcon(icon5)
        self.settings_1.setIconSize(QSize(100, 20))
        self.settings_1.setCheckable(True)
        self.settings_1.setChecked(False)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.settings_1)

        self.sign_out_1 = QPushButton(self.icon_only_widget)
        self.sign_out_1.setObjectName(u"sign_out_1")
        icon6 = QIcon()
        icon6.addFile(u":/images/signoutsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/images/signoutsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.sign_out_1.setIcon(icon6)
        self.sign_out_1.setIconSize(QSize(100, 16))
        self.sign_out_1.setCheckable(True)
        self.sign_out_1.setChecked(False)
        self.sign_out_1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.sign_out_1)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.layoutWidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setStyleSheet(u"QWidget {\n"
"background-color: rgb(0, 0, 0);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 30px;\n"
"	border: none\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, -1, -1)
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/images/logo (1).png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_text_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setStyleSheet(u"QPushButton {\n"
"	padding-left: -60px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-radius: 3px;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/images/dashboard2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/images/dashboard1.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_2.setIcon(icon7)
        self.dashboard_2.setIconSize(QSize(100, 60))
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoRepeat(False)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.dashboard_2)

        self.institution_2 = QPushButton(self.icon_text_widget)
        self.institution_2.setObjectName(u"institution_2")
        self.institution_2.setStyleSheet(u"QPushButton {\n"
"	padding-left: -65px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-radius: 3px;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/images/institution2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/images/institution1.png", QSize(), QIcon.Normal, QIcon.On)
        self.institution_2.setIcon(icon8)
        self.institution_2.setIconSize(QSize(95, 45))
        self.institution_2.setCheckable(True)
        self.institution_2.setAutoRepeat(False)
        self.institution_2.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.institution_2)

        self.students = QFrame(self.icon_text_widget)
        self.students.setObjectName(u"students")
        self.students.setFrameShape(QFrame.StyledPanel)
        self.students.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.students)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.students_2 = QPushButton(self.students)
        self.students_2.setObjectName(u"students_2")
        icon9 = QIcon()
        icon9.addFile(u":/images/students3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/images/students4.png", QSize(), QIcon.Normal, QIcon.On)
        self.students_2.setIcon(icon9)
        self.students_2.setIconSize(QSize(200, 60))
        self.students_2.setCheckable(True)
        self.students_2.setChecked(False)
        self.students_2.setAutoRepeat(False)
        self.students_2.setAutoExclusive(False)
        self.students_2.setAutoRepeatInterval(100)

        self.verticalLayout_4.addWidget(self.students_2)

        self.students_dropdown = QFrame(self.students)
        self.students_dropdown.setObjectName(u"students_dropdown")
        self.students_dropdown.setFrameShape(QFrame.StyledPanel)
        self.students_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.students_dropdown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.student_info = QPushButton(self.students_dropdown)
        self.student_info.setObjectName(u"student_info")
        self.student_info.setStyleSheet(u"QPushButton {\n"
"	padding-left: 20;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #12B29B\n"
"}")
        self.student_info.setCheckable(True)

        self.verticalLayout_2.addWidget(self.student_info)

        self.student_pay = QPushButton(self.students_dropdown)
        self.student_pay.setObjectName(u"student_pay")
        self.student_pay.setStyleSheet(u"QPushButton {\n"
"	padding-left: 11;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #12B29B\n"
"}")
        self.student_pay.setCheckable(True)

        self.verticalLayout_2.addWidget(self.student_pay)

        self.student_transaction = QPushButton(self.students_dropdown)
        self.student_transaction.setObjectName(u"student_transaction")
        self.student_transaction.setStyleSheet(u"QPushButton {\n"
"	padding-left: 25;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #12B29B\n"
"}")
        self.student_transaction.setCheckable(True)

        self.verticalLayout_2.addWidget(self.student_transaction)


        self.verticalLayout_4.addWidget(self.students_dropdown)


        self.verticalLayout_7.addWidget(self.students)

        self.teachers = QFrame(self.icon_text_widget)
        self.teachers.setObjectName(u"teachers")
        self.teachers.setFrameShape(QFrame.StyledPanel)
        self.teachers.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.teachers)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.teachers_2 = QPushButton(self.teachers)
        self.teachers_2.setObjectName(u"teachers_2")
        font1 = QFont()
        font1.setKerning(True)
        self.teachers_2.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/images/teachers3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/images/teachers4.png", QSize(), QIcon.Normal, QIcon.On)
        self.teachers_2.setIcon(icon10)
        self.teachers_2.setIconSize(QSize(200, 60))
        self.teachers_2.setCheckable(True)
        self.teachers_2.setChecked(False)
        self.teachers_2.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.teachers_2)

        self.teachers_dropdown = QFrame(self.teachers)
        self.teachers_dropdown.setObjectName(u"teachers_dropdown")
        self.teachers_dropdown.setFrameShape(QFrame.StyledPanel)
        self.teachers_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.teachers_dropdown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.teacher_info = QPushButton(self.teachers_dropdown)
        self.teacher_info.setObjectName(u"teacher_info")
        self.teacher_info.setStyleSheet(u"QPushButton {\n"
"	padding-left: 20;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #12B29B\n"
"}")
        self.teacher_info.setCheckable(True)

        self.verticalLayout.addWidget(self.teacher_info)

        self.teacher_salary = QPushButton(self.teachers_dropdown)
        self.teacher_salary.setObjectName(u"teacher_salary")
        self.teacher_salary.setStyleSheet(u"QPushButton {\n"
"	padding-left: -4;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #12B29B\n"
"}")
        self.teacher_salary.setCheckable(True)

        self.verticalLayout.addWidget(self.teacher_salary)

        self.teacher_transaction = QPushButton(self.teachers_dropdown)
        self.teacher_transaction.setObjectName(u"teacher_transaction")
        self.teacher_transaction.setStyleSheet(u"QPushButton {\n"
"	padding-left: 23;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #12B29B\n"
"}")
        self.teacher_transaction.setCheckable(True)

        self.verticalLayout.addWidget(self.teacher_transaction)


        self.verticalLayout_5.addWidget(self.teachers_dropdown)


        self.verticalLayout_7.addWidget(self.teachers)

        self.finances = QFrame(self.icon_text_widget)
        self.finances.setObjectName(u"finances")
        self.finances.setFrameShape(QFrame.StyledPanel)
        self.finances.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.finances)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.finance_2 = QPushButton(self.finances)
        self.finance_2.setObjectName(u"finance_2")
        icon11 = QIcon()
        icon11.addFile(u":/images/finances3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/images/finances4.png", QSize(), QIcon.Normal, QIcon.On)
        self.finance_2.setIcon(icon11)
        self.finance_2.setIconSize(QSize(200, 100))
        self.finance_2.setCheckable(True)
        self.finance_2.setChecked(False)
        self.finance_2.setAutoExclusive(False)

        self.verticalLayout_6.addWidget(self.finance_2)

        self.finance_dropdown = QFrame(self.finances)
        self.finance_dropdown.setObjectName(u"finance_dropdown")
        self.finance_dropdown.setFrameShape(QFrame.StyledPanel)
        self.finance_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.finance_dropdown)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.budgets = QPushButton(self.finance_dropdown)
        self.budgets.setObjectName(u"budgets")
        self.budgets.setStyleSheet(u"QPushButton {\n"
"	padding-left: -40;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #12B29B\n"
"}")
        self.budgets.setCheckable(True)

        self.verticalLayout_3.addWidget(self.budgets)

        self.expenses = QPushButton(self.finance_dropdown)
        self.expenses.setObjectName(u"expenses")
        self.expenses.setStyleSheet(u"QPushButton {\n"
"	padding-left: -33;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #12B29B\n"
"}")
        self.expenses.setCheckable(True)

        self.verticalLayout_3.addWidget(self.expenses)

        self.business_overview = QPushButton(self.finance_dropdown)
        self.business_overview.setObjectName(u"business_overview")
        self.business_overview.setStyleSheet(u"QPushButton {\n"
"	padding-left: 15;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #12B29B\n"
"}")
        self.business_overview.setCheckable(True)
        self.business_overview.setChecked(False)
        self.business_overview.setAutoRepeat(False)
        self.business_overview.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.business_overview)


        self.verticalLayout_6.addWidget(self.finance_dropdown)


        self.verticalLayout_7.addWidget(self.finances)


        self.verticalLayout_11.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 77, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.settings_2 = QPushButton(self.icon_text_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setStyleSheet(u"QPushButton {\n"
"	padding-left: -65px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-radius: 3px;\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/images/settings2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon12.addFile(u":/images/settings1.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_2.setIcon(icon12)
        self.settings_2.setIconSize(QSize(100, 60))
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.settings_2)

        self.sign_out_2 = QPushButton(self.icon_text_widget)
        self.sign_out_2.setObjectName(u"sign_out_2")
        self.sign_out_2.setStyleSheet(u"QPushButton {\n"
"	padding-left: -60px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-radius: 3px;\n"
"}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/images/signout2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/images/signout1.png", QSize(), QIcon.Normal, QIcon.On)
        self.sign_out_2.setIcon(icon13)
        self.sign_out_2.setIconSize(QSize(100, 60))
        self.sign_out_2.setCheckable(True)
        self.sign_out_2.setAutoExclusive(False)

        self.verticalLayout_8.addWidget(self.sign_out_2)


        self.verticalLayout_11.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border:none;")
        icon14 = QIcon()
        icon14.addFile(u":/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 25, -1, 25)
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.label)

        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setPointSize(10)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color:grey;")

        self.verticalLayout_13.addWidget(self.label_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_13)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(295, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 25, -1)
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(340, 31))
        self.lineEdit.setMaximumSize(QSize(340, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	padding-left:20;\n"
"	border: 1 solid gray;\n"
"	border-radius: 10;\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.header_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 40))
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/images/profile1.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_14.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.layoutWidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(920, 741))
        self.main_screen_widget.setMaximumSize(QSize(920, 741))
        self.main_screen_widget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 901, 741))
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(1111111, 1111111))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(360, 300, 181, 141))
        font4 = QFont()
        font4.setPointSize(25)
        self.label_7.setFont(font4)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(360, 300, 181, 141))
        self.label_8.setFont(font4)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 0, 211, 31))
        font5 = QFont()
        font5.setPointSize(25)
        font5.setBold(True)
        self.label_9.setFont(font5)
        self.label_19 = QLabel(self.page_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 40, 561, 31))
        font6 = QFont()
        font6.setPointSize(9)
        self.label_19.setFont(font6)
        self.studentInfo_table = QTableWidget(self.page_3)
        if (self.studentInfo_table.columnCount() < 10):
            self.studentInfo_table.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.studentInfo_table.setObjectName(u"studentInfo_table")
        self.studentInfo_table.setGeometry(QRect(10, 200, 950, 521))
        self.studentInfo_table.setStyleSheet(u"QHeaderView::section {\n"
"	font-weight: bold;\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableWidget {\n"
"	alternate-background-color: #B0BDFB;\n"
"	background-color:#F4F9FA;\n"
"}")
        self.studentInfo_table.setAlternatingRowColors(True)
        self.widget = QWidget(self.page_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 70, 431, 43))
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.addStudent_btn = QPushButton(self.widget)
        self.addStudent_btn.setObjectName(u"addStudent_btn")
        self.addStudent_btn.setMinimumSize(QSize(111, 41))
        font7 = QFont()
        font7.setBold(True)
        self.addStudent_btn.setFont(font7)
        self.addStudent_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:black;\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 8;\n"
"	font-weight: bold;\n"
"	font-size:15px;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/images/add student.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addStudent_btn.setIcon(icon15)

        self.horizontalLayout_6.addWidget(self.addStudent_btn)

        self.excelExport_btn = QPushButton(self.widget)
        self.excelExport_btn.setObjectName(u"excelExport_btn")
        self.excelExport_btn.setMinimumSize(QSize(111, 41))
        self.excelExport_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:#34D481;\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 8;\n"
"	font-weight: bold;\n"
"	font-size:15px;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/images/excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.excelExport_btn.setIcon(icon16)

        self.horizontalLayout_6.addWidget(self.excelExport_btn)

        self.pdfExport_btn = QPushButton(self.widget)
        self.pdfExport_btn.setObjectName(u"pdfExport_btn")
        self.pdfExport_btn.setMinimumSize(QSize(75, 41))
        self.pdfExport_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:#ff4e4e;\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 8;\n"
"	font-weight: bold;\n"
"	font-size:15px;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/images/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pdfExport_btn.setIcon(icon17)

        self.horizontalLayout_6.addWidget(self.pdfExport_btn)

        self.widget1 = QWidget(self.page_3)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 140, 654, 41))
        self.horizontalLayout_7 = QHBoxLayout(self.widget1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.select_gender = QComboBox(self.widget1)
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.setObjectName(u"select_gender")
        self.select_gender.setMinimumSize(QSize(150, 0))
        self.select_gender.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid white;\n"
"	border-radius: 8;\n"
"	padding: 1 18 1 15;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	height: 35;\n"
"	font-weight: bold;\n"
"	selection-background-color: #2980B9\n"
"}")

        self.horizontalLayout_7.addWidget(self.select_gender)

        self.select_class = QComboBox(self.widget1)
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.setObjectName(u"select_class")
        self.select_class.setMinimumSize(QSize(150, 0))
        self.select_class.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid white;\n"
"	border-radius: 8;\n"
"	padding: 1 18 1 15;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	height: 35;\n"
"	font-weight: bold;\n"
"	selection-background-color: #2980B9\n"
"}")

        self.horizontalLayout_7.addWidget(self.select_class)

        self.search_student = QLineEdit(self.widget1)
        self.search_student.setObjectName(u"search_student")
        self.search_student.setMinimumSize(QSize(340, 38))
        self.search_student.setMaximumSize(QSize(340, 38))
        self.search_student.setStyleSheet(u"QLineEdit {\n"
"	padding-left:20;\n"
"	border: 1 solid gray;\n"
"	border-radius: 10;\n"
"}")

        self.horizontalLayout_7.addWidget(self.search_student)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(330, 340, 261, 141))
        self.label_10.setFont(font4)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(320, 320, 291, 141))
        self.label_11.setFont(font4)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(300, 340, 181, 141))
        self.label_12.setFont(font4)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(300, 340, 231, 141))
        self.label_13.setFont(font4)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_14 = QLabel(self.page_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(300, 330, 291, 141))
        self.label_14.setFont(font4)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_15 = QLabel(self.page_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(300, 330, 181, 141))
        self.label_15.setFont(font4)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_16 = QLabel(self.page_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(340, 340, 181, 141))
        self.label_16.setFont(font4)
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.label_17 = QLabel(self.page_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(340, 360, 271, 141))
        self.label_17.setFont(font4)
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_18 = QLabel(self.page_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(310, 350, 181, 141))
        self.label_18.setFont(font4)
        self.stackedWidget.addWidget(self.page_12)

        self.verticalLayout_14.addWidget(self.main_screen_widget)


        self.gridLayout.addLayout(self.verticalLayout_14, 0, 2, 1, 1)


        self.retranslateUi(Form)
        self.students_2.toggled.connect(self.students_dropdown.setHidden)
        self.teachers_2.toggled.connect(self.teachers_dropdown.setHidden)
        self.finance_2.toggled.connect(self.finance_dropdown.setHidden)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.institution_2.toggled.connect(self.institution_1.setChecked)
        self.students_2.toggled.connect(self.students_1.setChecked)
        self.teachers_2.toggled.connect(self.teachers_1.setChecked)
        self.finance_2.toggled.connect(self.finance_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.sign_out_2.toggled.connect(self.sign_out_1.setChecked)
        self.sign_out_1.toggled.connect(Form.close)
        self.sign_out_2.toggled.connect(Form.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText("")
        self.dashboard_1.setText("")
        self.institution_1.setText("")
        self.students_1.setText("")
        self.teachers_1.setText("")
        self.finance_1.setText("")
        self.settings_1.setText("")
        self.sign_out_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"School", None))
        self.dashboard_2.setText("")
        self.institution_2.setText("")
        self.students_2.setText("")
        self.student_info.setText(QCoreApplication.translate("Form", u"Student Information", None))
        self.student_pay.setText(QCoreApplication.translate("Form", u"Student Payments", None))
        self.student_transaction.setText(QCoreApplication.translate("Form", u"Student Transactions", None))
        self.teachers_2.setText("")
        self.teacher_info.setText(QCoreApplication.translate("Form", u"Teacher Information", None))
        self.teacher_salary.setText(QCoreApplication.translate("Form", u"Teacher salaries", None))
        self.teacher_transaction.setText(QCoreApplication.translate("Form", u"Teacher Transactions", None))
        self.finance_2.setText("")
        self.budgets.setText(QCoreApplication.translate("Form", u"Budgets", None))
        self.expenses.setText(QCoreApplication.translate("Form", u"Expenses", None))
        self.business_overview.setText(QCoreApplication.translate("Form", u"Business Overview", None))
        self.settings_2.setText("")
        self.sign_out_2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Hello, Java", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Welcome to your page", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Search Here...", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Institution", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Student info", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Welcome to the students information page", None))
        ___qtablewidgetitem = self.studentInfo_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem1 = self.studentInfo_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Student ID", None));
        ___qtablewidgetitem2 = self.studentInfo_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Gender", None));
        ___qtablewidgetitem3 = self.studentInfo_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Class", None));
        ___qtablewidgetitem4 = self.studentInfo_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Birthday", None));
        ___qtablewidgetitem5 = self.studentInfo_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Age", None));
        ___qtablewidgetitem6 = self.studentInfo_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Address", None));
        ___qtablewidgetitem7 = self.studentInfo_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Phone", None));
        ___qtablewidgetitem8 = self.studentInfo_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Email", None));
        ___qtablewidgetitem9 = self.studentInfo_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Actions", None));
        self.addStudent_btn.setText(QCoreApplication.translate("Form", u"Add Student", None))
        self.excelExport_btn.setText(QCoreApplication.translate("Form", u"Export to Excel", None))
        self.pdfExport_btn.setText(QCoreApplication.translate("Form", u"Export to PDF", None))
        self.select_gender.setItemText(0, QCoreApplication.translate("Form", u"SELECT GENDER", None))
        self.select_gender.setItemText(1, QCoreApplication.translate("Form", u"Male", None))
        self.select_gender.setItemText(2, QCoreApplication.translate("Form", u"Female", None))

        self.select_class.setItemText(0, QCoreApplication.translate("Form", u"SELECT CLASS", None))
        self.select_class.setItemText(1, QCoreApplication.translate("Form", u"Grade 1", None))
        self.select_class.setItemText(2, QCoreApplication.translate("Form", u"Grade 2", None))
        self.select_class.setItemText(3, QCoreApplication.translate("Form", u"Grade 3", None))
        self.select_class.setItemText(4, QCoreApplication.translate("Form", u"Grade 4", None))
        self.select_class.setItemText(5, QCoreApplication.translate("Form", u"Grade 5", None))
        self.select_class.setItemText(6, QCoreApplication.translate("Form", u"Grade 6", None))
        self.select_class.setItemText(7, QCoreApplication.translate("Form", u"Grade 7", None))
        self.select_class.setItemText(8, QCoreApplication.translate("Form", u"Grade 8", None))
        self.select_class.setItemText(9, QCoreApplication.translate("Form", u"Grade 9", None))
        self.select_class.setItemText(10, QCoreApplication.translate("Form", u"Grade 10", None))
        self.select_class.setItemText(11, QCoreApplication.translate("Form", u"Grade 11", None))

        self.search_student.setPlaceholderText(QCoreApplication.translate("Form", u"Search Student...", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Student payment", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Student transaction", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Teacher info", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Teacher salaries", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Teacher transaction", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Budgets", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Expenses", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Business Overview", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Settings", None))
    # retranslateUi

