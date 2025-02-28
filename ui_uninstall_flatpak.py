# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uninstall_flatpak.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Uninstall_Flatpak(object):
    def setupUi(self, Uninstall_Flatpak):
        if not Uninstall_Flatpak.objectName():
            Uninstall_Flatpak.setObjectName(u"Uninstall_Flatpak")
        Uninstall_Flatpak.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"icons/256x256.png", QSize(), QIcon.Normal, QIcon.Off)
        Uninstall_Flatpak.setWindowIcon(icon)
        self.pushButton_yes_user = QPushButton(Uninstall_Flatpak)
        self.pushButton_yes_user.setObjectName(u"pushButton_yes_user")
        self.pushButton_yes_user.setGeometry(QRect(582, 510, 111, 41))
        self.pushButton_yes_system = QPushButton(Uninstall_Flatpak)
        self.pushButton_yes_system.setObjectName(u"pushButton_yes_system")
        self.pushButton_yes_system.setGeometry(QRect(432, 510, 111, 41))
        self.lineEdit = QLineEdit(Uninstall_Flatpak)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(84, 180, 611, 27))
        self.label = QLabel(Uninstall_Flatpak)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 40, 601, 91))
        self.pushButton_no = QPushButton(Uninstall_Flatpak)
        self.pushButton_no.setObjectName(u"pushButton_no")
        self.pushButton_no.setGeometry(QRect(280, 510, 111, 41))

        self.retranslateUi(Uninstall_Flatpak)
        self.pushButton_no.clicked.connect(Uninstall_Flatpak.reject)

        QMetaObject.connectSlotsByName(Uninstall_Flatpak)
    # setupUi

    def retranslateUi(self, Uninstall_Flatpak):
        Uninstall_Flatpak.setWindowTitle(QCoreApplication.translate("Uninstall_Flatpak", u"Dialog", None))
        self.pushButton_yes_user.setText(QCoreApplication.translate("Uninstall_Flatpak", u"\u786e\u5b9a\uff08\u7528\u6237\u7ea7\uff09", None))
        self.pushButton_yes_system.setText(QCoreApplication.translate("Uninstall_Flatpak", u"\u786e\u5b9a\uff08\u7cfb\u7edf\u7ea7\uff09", None))
        self.lineEdit.setText(QCoreApplication.translate("Uninstall_Flatpak", u"\u4fee\u6539\u6b64\u5904\u6587\u5b57\u4fee\u6539\u4e3a\u4f60\u8981\u5378\u8f7d\u7684\u8f6f\u4ef6\u540d\u79f0\uff08\u652f\u6301\u591a\u4e2a\uff0c\u7528\u7a7a\u683c\u9694\u5f00\uff09", None))
        self.label.setText(QCoreApplication.translate("Uninstall_Flatpak", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">\u5378\u8f7d</span></p></body></html>", None))
        self.pushButton_no.setText(QCoreApplication.translate("Uninstall_Flatpak", u"\u53d6\u6d88", None))
    # retranslateUi

