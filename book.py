# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_book_screen(object):
    def setupUi(self, book_screen):
        book_screen.setObjectName("book_screen")
        book_screen.resize(800, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(book_screen.sizePolicy().hasHeightForWidth())
        book_screen.setSizePolicy(sizePolicy)
        book_screen.setMinimumSize(QtCore.QSize(800, 800))
        book_screen.setMaximumSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(book_screen)
        self.centralwidget.setObjectName("centralwidget")
        self.dic_character = QtWidgets.QLabel(self.centralwidget)
        self.dic_character.setGeometry(QtCore.QRect(420, 190, 231, 351))
        self.dic_character.setStyleSheet("font-size:20px;\n"
"")
        self.dic_character.setScaledContents(True)
        self.dic_character.setWordWrap(True)
        self.dic_character.setObjectName("dic_character")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, 0, 821, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imgs/livro.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.back_tofirst = QtWidgets.QPushButton(self.centralwidget)
        self.back_tofirst.setGeometry(QtCore.QRect(310, 670, 191, 31))
        self.back_tofirst.setStyleSheet("font-size:15px;\n"
"background-color:#B1AF74;")
        self.back_tofirst.setObjectName("back_tofirst")
        self.label.raise_()
        self.dic_character.raise_()
        self.back_tofirst.raise_()
        book_screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(book_screen)
        QtCore.QMetaObject.connectSlotsByName(book_screen)

    def retranslateUi(self, book_screen):
        _translate = QtCore.QCoreApplication.translate
        book_screen.setWindowTitle(_translate("book_screen", "MainWindow"))
        self.dic_character.setText(_translate("book_screen", "\n"
"\n"
"existe um filme conhecido por todos onde tem um personagem que diz: \"espelho espelho meu existe alguem mais bonito que eu?\" \n"
"\n"
"\n"
"que objeto está relacionado a este filme?\n"
"Guarde essa letra: U"))
        self.back_tofirst.setText(_translate("book_screen", "Volte para a primeira página"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    book_screen = QtWidgets.QMainWindow()
    ui = Ui_book_screen()
    ui.setupUi(book_screen)
    book_screen.show()
    sys.exit(app.exec_())
