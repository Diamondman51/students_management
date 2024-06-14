# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerJsWXam.ui'
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
        Form.resize(503, 26)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 501, 26))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.btn_first = QPushButton(self.widget)
        self.btn_first.setObjectName(u"btn_first")

        self.horizontalLayout.addWidget(self.btn_first)

        self.btn_previous = QPushButton(self.widget)
        self.btn_previous.setObjectName(u"btn_previous")

        self.horizontalLayout.addWidget(self.btn_previous)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(60, 16777215))
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.btn_next = QPushButton(self.widget)
        self.btn_next.setObjectName(u"btn_next")

        self.horizontalLayout.addWidget(self.btn_next)

        self.btn_last = QPushButton(self.widget)
        self.btn_last.setObjectName(u"btn_last")

        self.horizontalLayout.addWidget(self.btn_last)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"00", None))
        self.btn_first.setText(QCoreApplication.translate("Form", u"<<", None))
        self.btn_previous.setText(QCoreApplication.translate("Form", u"<", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"1", None))
        self.btn_next.setText(QCoreApplication.translate("Form", u">", None))
        self.btn_last.setText(QCoreApplication.translate("Form", u">>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"123", None))
    # retranslateUi

