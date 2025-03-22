# Form implementation generated from reading ui file 'uninstall.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from uninstall_pacman import *
from uninstall_flatpak import *


class Ui_Uninstall(object):
    def setupUi(self, Uninstall):
        Uninstall.setObjectName("Uninstall")
        Uninstall.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/256x256.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Uninstall.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(parent=Uninstall)
        self.pushButton.setGeometry(QtCore.QRect(120, 162, 551, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Pacman_Uninstall)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Uninstall)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 332, 551, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(parent=Uninstall)
        self.label.setGeometry(QtCore.QRect(120, 40, 551, 81))
        self.label.setObjectName("label")

        self.retranslateUi(Uninstall)
        QtCore.QMetaObject.connectSlotsByName(Uninstall)

    def retranslateUi(self, Uninstall):
        _translate = QtCore.QCoreApplication.translate
        Uninstall.setWindowTitle(_translate("Uninstall", "yay+ Uninstall MainWindow"))
        self.pushButton.setText(_translate("Uninstall", "卸载 Pacman 安装的软件（包括使用 makepkg 的 -i 参数安装的）"))
        self.pushButton_2.setText(_translate("Uninstall", "卸载 Flatpak 安装的软件"))
        self.label.setText(_translate("Uninstall", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">卸载</span></p></body></html>"))

    def Pacman_Uninstall(self):
        # 方法一：使用模态对话框（推荐）
        self.uninstall_dialog = QtWidgets.QDialog()
        self.ui_uninstall_pacman = Ui_Uninstall_Pacman()
        self.ui_uninstall_pacman.setupUi(self.uninstall_dialog)

        # 设置关闭时自动销毁
        self.uninstall_dialog.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose)

        # 连接对话框关闭信号
        self.uninstall_dialog.finished.connect(self.restore_main_window_pacman)

        # 设置为模态
        self.uninstall_dialog.exec()

    def Flatpak_Uninstall(self):
        # 方法一：使用模态对话框（推荐）
        self.uninstall_dialog = QtWidgets.QDialog()
        self.ui_uninstall_flatpak = Ui_Uninstall_Flatpak()
        self.ui_uninstall_flatpak.setupUi(self.uninstall_dialog)
        # 设置关闭时自动销毁
        self.uninstall_dialog.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose)
        # 连接对话框关闭信号
        self.uninstall_dialog.finished.connect(self.restore_main_window_flatpak)
        # 设置为模态
        self.uninstall_dialog.exec()

    def restore_main_window_pacman(self, result):
        print(self.tr("Pacman 卸载窗口已关闭，返回码:"), self.Ui_Uninstall_Pacman.exit_code)

    def restore_main_window_flatpak(self, result):
        print(self.tr("Flatpak 卸载窗口已关闭，返回码:"), self.Ui_Uninstall_Flatpak.exit_code)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Uninstall = QtWidgets.QDialog()
    ui = Ui_Uninstall()
    ui.setupUi(Uninstall)
    Uninstall.show()
    sys.exit(app.exec())
