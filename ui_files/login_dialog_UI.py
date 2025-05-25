# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_UIdnWBQq.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import resources.resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1058, 701)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(1058, 701))
        Dialog.setMaximumSize(QSize(1058, 701))
        Dialog.setStyleSheet(u"*{border:none}\n"
"\n"
"QDialog {\n"
"    border-image: url(':/images/back.png');\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: black;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"margin: 1 2 1 2;\n"
"}\n"
"\n"
"QLabel {\n"
"color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"border-radius:5;\n"
"padding:0 15;\n"
"}\n"
"\n"
"")
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.login_widget = QWidget(Dialog)
        self.login_widget.setObjectName(u"login_widget")
        self.login_widget.setMinimumSize(QSize(500, 0))
        self.login_widget.setStyleSheet(u"#login_widget {\n"
"	background-color: rgba(0, 112, 215, 0.4);\n"
"	border-radius: 15;\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.login_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 9, 1, 1, 1)

        self.label_3 = QLabel(self.login_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 0, 1, 3)

        self.pushButton_2 = QPushButton(self.login_widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 35))
        icon = QIcon()
        icon.addFile(u":/images/google_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_2, 8, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.login_widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 35))
        icon1 = QIcon()
        icon1.addFile(u":/images/facebook_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon1)

        self.gridLayout.addWidget(self.pushButton_4, 8, 2, 1, 1)

        self.password_line = QLineEdit(self.login_widget)
        self.password_line.setObjectName(u"password_line")
        self.password_line.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setStrikeOut(False)
        self.password_line.setFont(font1)

        self.gridLayout.addWidget(self.password_line, 4, 0, 1, 3)

        self.pushButton_3 = QPushButton(self.login_widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 35))
        icon2 = QIcon()
        icon2.addFile(u":/images/github_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.gridLayout.addWidget(self.pushButton_3, 8, 1, 1, 1)

        self.email_Line = QLineEdit(self.login_widget)
        self.email_Line.setFocus()
        self.email_Line.setObjectName(u"email_Line")
        self.email_Line.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.email_Line, 2, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 3)

        self.label_2 = QLabel(self.login_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)

        self.label = QLabel(self.login_widget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.sign_in_btn = QPushButton(self.login_widget)
        self.sign_in_btn.setObjectName(u"sign_in_btn")
        self.sign_in_btn.setMinimumSize(QSize(0, 35))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        self.sign_in_btn.setFont(font3)

        self.gridLayout.addWidget(self.sign_in_btn, 6, 0, 1, 3)

        self.password_line.raise_()
        self.email_Line.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.sign_in_btn.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()

        self.gridLayout_2.addWidget(self.login_widget, 1, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 2, 1, 1, 1)

        QWidget.setTabOrder(self.email_Line, self.password_line)
        QWidget.setTabOrder(self.password_line, self.sign_in_btn)
        QWidget.setTabOrder(self.sign_in_btn, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_4)

        self.retranslateUi(Dialog)

        self.sign_in_btn.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Parol", None))
        self.pushButton_2.setText("")
        self.pushButton_4.setText("")
        self.password_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.pushButton_3.setText("")
        self.email_Line.setPlaceholderText(QCoreApplication.translate("Dialog", u"username@gmail.com", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.sign_in_btn.setText(QCoreApplication.translate("Dialog", u"Sign in", None))


