# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_second(object):
    def setupUi(self, second):
        second.setObjectName("second")
        second.resize(800, 800)
        second.setMinimumSize(QtCore.QSize(800, 800))
        second.setMaximumSize(QtCore.QSize(800, 800))
        second.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(second)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 800))
        self.label.setMinimumSize(QtCore.QSize(800, 800))
        self.label.setMaximumSize(QtCore.QSize(800, 800))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imgs/1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 150, 771, 181))
        self.label_2.setStyleSheet("font-size: 18px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 240, 671, 171))
        self.label_3.setStyleSheet("font-size: 18px;")
        self.label_3.setObjectName("label_3")
        self.first_error = QtWidgets.QPushButton(self.centralwidget)
        self.first_error.setGeometry(QtCore.QRect(260, 430, 31, 21))
        self.first_error.setStyleSheet("padding:25px;\n"
"font-size:15px;\n"
"background-color:#B1B175;")
        self.first_error.setObjectName("first_error")
        self.answer_correct = QtWidgets.QPushButton(self.centralwidget)
        self.answer_correct.setGeometry(QtCore.QRect(400, 430, 31, 21))
        self.answer_correct.setStyleSheet("padding:25px;\n"
"font-size:15px;\n"
"background-color:#B1B175;")
        self.answer_correct.setObjectName("answer_correct")
        self.second_error = QtWidgets.QPushButton(self.centralwidget)
        self.second_error.setGeometry(QtCore.QRect(330, 430, 31, 21))
        self.second_error.setStyleSheet("padding:25px;\n"
"font-size:15px;\n"
"background-color:#B1B175;")
        self.second_error.setObjectName("second_error")
        self.third_error = QtWidgets.QPushButton(self.centralwidget)
        self.third_error.setGeometry(QtCore.QRect(470, 430, 31, 21))
        self.third_error.setStyleSheet("padding:25px;\n"
"font-size:15px;\n"
"background-color:#B1B175;")
        self.third_error.setObjectName("third_error")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 360, 251, 51))
        self.label_4.setStyleSheet("font-size:20px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.correct_or_error = QtWidgets.QLabel(self.centralwidget)
        self.correct_or_error.setGeometry(QtCore.QRect(260, 660, 341, 51))
        self.correct_or_error.setStyleSheet("font-size:20px;\n"
"")
        self.correct_or_error.setText("")
        self.correct_or_error.setWordWrap(True)
        self.correct_or_error.setObjectName("correct_or_error")
        self.back_tofirst = QtWidgets.QPushButton(self.centralwidget)
        self.back_tofirst.setGeometry(QtCore.QRect(320, 740, 191, 31))
        self.back_tofirst.setStyleSheet("font-size:15px;\n"
"background-color:#B1AF74;")
        self.back_tofirst.setObjectName("back_tofirst")
        second.setCentralWidget(self.centralwidget)

        self.retranslateUi(second)
        QtCore.QMetaObject.connectSlotsByName(second)

    def retranslateUi(self, second):
        _translate = QtCore.QCoreApplication.translate
        second.setWindowTitle(_translate("second", "MainWindow"))
        self.label_2.setText(_translate("second", "Raciocinio lógico, de acordo com o resultado, encontre o próximo objeto. \n"
"26, 29, 33, 36, 40 \n"
""))
        self.label_3.setText(_translate("second", "\n"
"nesse raciocnio lógico existem dois padrões, qual é o segundo padrão?\n"
"É um valor inteiro. Depois de pensar, procure o objeto com essa quantia.\n"
""))
        self.first_error.setText(_translate("second", "20"))
        self.answer_correct.setText(_translate("second", "4"))
        self.second_error.setText(_translate("second", "2"))
        self.third_error.setText(_translate("second", "5"))
        self.label_4.setText(_translate("second", "Qual o segundo padrão?"))
        self.back_tofirst.setText(_translate("second", "Volte para a primeira página"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    second = QtWidgets.QMainWindow()
    ui = Ui_second()
    ui.setupUi(second)
    second.show()
    sys.exit(app.exec_())
