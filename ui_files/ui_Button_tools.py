# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'button_toolsIBlmIK.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(448, 44)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_passed_pages = QLabel(Form)
        self.lbl_passed_pages.setObjectName(u"lbl_passed_pages")

        self.horizontalLayout.addWidget(self.lbl_passed_pages)

        self.btn_first_page = QPushButton(Form)
        self.btn_first_page.setObjectName(u"btn_first_page")

        self.horizontalLayout.addWidget(self.btn_first_page)

        self.btn_previous_page = QPushButton(Form)
        self.btn_previous_page.setObjectName(u"btn_previous_page")

        self.horizontalLayout.addWidget(self.btn_previous_page)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.btn_next_page = QPushButton(Form)
        self.btn_next_page.setObjectName(u"btn_next_page")

        self.horizontalLayout.addWidget(self.btn_next_page)

        self.btn_last_page = QPushButton(Form)
        self.btn_last_page.setObjectName(u"btn_last_page")

        self.horizontalLayout.addWidget(self.btn_last_page)

        self.lbl_left_pages = QLabel(Form)
        self.lbl_left_pages.setObjectName(u"lbl_left_pages")

        self.horizontalLayout.addWidget(self.lbl_left_pages)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_passed_pages.setText(QCoreApplication.translate("Form", u"0", None))
        self.btn_first_page.setText(QCoreApplication.translate("Form", u"<<", None))
        self.btn_previous_page.setText(QCoreApplication.translate("Form", u"<", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"1", None))
        self.btn_next_page.setText(QCoreApplication.translate("Form", u">", None))
        self.btn_last_page.setText(QCoreApplication.translate("Form", u">>", None))
        self.lbl_left_pages.setText(QCoreApplication.translate("Form", u"1234", None))
    # retranslateUi

