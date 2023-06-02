from PyQt5 import uic, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
from tela import Ui_MainWindow
from second import Ui_second
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets

class First(Ui_MainWindow):
    def __init__(self, MainWindow) -> None:
        self.setupUi(MainWindow)
        self.start.clicked.connect(self.start_the)
        self.computer.clicked.connect(self.second_dic)
       
        
    def start_the(self):
        self.first_dic.setText("Welcome to the game! Scape room.\nThe first dic is: what in the room is related to Alan Turing?")

        
    def second_dic(self):
        second.show()
        window.close()
        
    
class Second(Ui_second):
    def __init__(self, second):
        self.setupUi(second)
        self.backfirst.clicked.connect(self.back_firstWindow)
        
    def back_firstWindow(self):
        window.show()
        second.close()
        
  
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    screen = First(window)
    window.show()
    
    second = QtWidgets.QMainWindow()
    ui = Ui_second()
    second_screen = Second(second)
   
    sys.exit(app.exec_())


