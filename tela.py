# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setStyleSheet("background-color: #B1AF76;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbprincipal = QtWidgets.QLabel(self.centralwidget)
        self.lbprincipal.setGeometry(QtCore.QRect(280, 0, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lbprincipal.setFont(font)
        self.lbprincipal.setStyleSheet("font-size:35px\n"
";")
        self.lbprincipal.setObjectName("lbprincipal")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(330, 710, 191, 41))
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start.setStyleSheet("font-size:25px;")
        self.start.setFlat(False)
        self.start.setObjectName("start")
        self.first_dic = QtWidgets.QLabel(self.centralwidget)
        self.first_dic.setGeometry(QtCore.QRect(0, 650, 801, 61))
        self.first_dic.setStyleSheet("background-color: #DABBB9;\n"
"font-size: 15px;")
        self.first_dic.setText("")
        self.first_dic.setObjectName("first_dic")
        self.computer = QtWidgets.QPushButton(self.centralwidget)
        self.computer.setGeometry(QtCore.QRect(70, 330, 41, 51))
        self.computer.setStyleSheet("background-color:#313F6E;")
        self.computer.setText("")
        self.computer.setFlat(True)
        self.computer.setObjectName("computer")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 800, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(800, 700))
        self.label_2.setMaximumSize(QtCore.QSize(800, 700))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("fundo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 430, 56, 17))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 710, 801, 101))
        self.label.setStyleSheet("background-color:#DABBB9;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.label_2.raise_()
        self.lbprincipal.raise_()
        self.start.raise_()
        self.pushButton.raise_()
        self.first_dic.raise_()
        self.computer.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "teste"))
        self.lbprincipal.setText(_translate("MainWindow", "Scape room"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())