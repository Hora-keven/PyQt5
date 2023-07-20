from PyQt5 import uic, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
from tela import Ui_MainWindow
from second import Ui_second
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from book import Ui_book_screen
from fourth import Ui_mirror
from lasttip import Ui_shine
from penultimateScreen import Ui_verification
from final import Ui_outhome
from maçaneta import Ui_key
from error import Ui_erro
from play_error import Ui_play_error
from threading import *
import pygame
import time
import musics


class First(Ui_MainWindow):
    def __init__(self, MainWindow) -> None:
        self.setupUi(MainWindow)
        self.desative()
        self.start.clicked.connect(self.start_dic)
        self.computer.clicked.connect(self.second_tip)
        self.book.clicked.connect(self.third_tip)
        self.mirror_tip.clicked.connect(self.fourth_tip)
        self.lastpag.clicked.connect(self.last_tip)
        self.keys_win.clicked.connect(self.key)
        self.out.clicked.connect(self.playground)
        self.noright.clicked.connect(self.clik_error)
        self.noright_2.clicked.connect(self.clik_error)
        self.table.clicked.connect(self.clik_error)
       

    def desative(self):
        self.out.setHidden(True)
        self.keys_win.setHidden(True)
        self.computer.setHidden(False)
        self.mirror_tip.setHidden(True)
        self.lastpag.setHidden(True)
        self.out.setHidden(True)
        self.book.setHidden(True)
    
    def start_dic(self):
        self.first_dic.setText("  Bem-vindo ao jogo! Scape room. A primeira dica é: o que na sala tem a ver com Alan Turing? guarde essa letra: H")
     

    def clik_error(self):
        error_play.show()
        window.close()
        musics.thread_error()
      
    def second_tip(self):
        self.first_dic.clear()
        self.computer.setHidden(True)
        self.book.setHidden(False)
        window.close()
        second.show()
        musics.thread_computer()
 
    def third_tip(self):
        self.book.setHidden(True)
        second.close()
        window.close()
        book_screen.show()
        self.mirror_tip.setHidden(False)
        musics.thread_book()
        
    def fourth_tip(self):
        self.mirror_tip.setHidden(True)
        self.lastpag.setHidden(False)
        book_screen.close()
        window.close()
        mirror_screen.show()

    def last_tip(self):
     
        musics.thread_idea()
        mirror_screen.close()
        window.close()
        self.lastpag.setHidden(True)
        self.keys_win.setHidden(False)
        penultimate_screen.show()
        
    def key(self):
        self.keys_win.setHidden(True)
        penultimate_screen.close()
        self.out.setHidden(False)
        window.close()
        key.show()
        
    def playground(self):
        key.close()
        window.close()
        final.show()
        musics.thread_playground()

    
class Second(Ui_second):
    def __init__(self, second):
        self.setupUi(second)
        self.answer_correct.clicked.connect(self.correct)
        self.first_error.clicked.connect(self.error)
        self.second_error.clicked.connect(self.error)
        self.third_error.clicked.connect(self.error)
        
    def back_tofirstpage(self):
         window.show()
         second.close()
        
    def error(self):
        self.is_false()
        self.correct_or_error.setText("Você errou! tente novamente")
        musics.thread_error()
        self.back_tofirst.setEnabled(True)

    def correct(self):
        musics.thread_right()
        self.correct_or_error.setText(f"Você acertou! guarde essa letra: P. Agora volte para a primeira página")
        self.back_tofirst.setHidden(False)
        self.back_tofirst.clicked.connect(self.back_tofirstpage)

        
    def is_false(self):
        screen_error.show()
        musics.thread_error()
        second.close()
            
class Screen_Book(Ui_book_screen):
    def __init__(self, book_screen):
        self.setupUi(book_screen)
        self.back_tofirst.clicked.connect(self.back_topage)

    def back_topage(self):
        book_screen.close()   
        window.show()

class Screen_mirror(Ui_mirror):
    def __init__(self, screen_mirror) -> None:
        self.setupUi(screen_mirror)
        
        self.back_tofirst.clicked.connect(self.back_topage)
        
    def back_topage(self):
        mirror_screen.close()   
        window.show()
          
class Penultimate_screen(Ui_shine):
    def __init__(self, penultimate_screen) -> None:
        self.setupUi(penultimate_screen)
        
        self.proximapag.clicked.connect(self.next_page)
        
    def next_page(self):
        window.close()
        penultimate_screen.close()
        last_tip.show()
        
class Last_tip(Ui_verification):
    def __init__(self, last_tip) -> None:
        self.setupUi(last_tip)
        self.question_user()
        self.validation.clicked.connect(self.right_error)
        
    def question_user(self):
        self.question.setText("   Com as letras que você viu ao longo do jogo, onde está a chave?")
        
    def right_error(self):
        reposta = self.iinput_usuario.text()
        if reposta == 'plush' or reposta == 'PLUSH':
            self.correct_error.setText('   Parabéns você acertou! Agora procure o Plush. ')
            musics.thread_right()
            last_tip.close()
            window.show()
        else:
            self.correct_error.setText("   Errado. Na ordem as letras foram: H, P, U, L, S ")
            musics.thread_user()
           
class Key(Ui_key):
    def __init__(self, key) -> None:
        self.setupUi(key)
        self.out_home.clicked.connect(self.final_screen)
        
    def final_screen(self):
        window.show()
        key.close()     
        
class Final(Ui_outhome): 
    def __init__(self, out) -> None:
          self.setupUi(out)


class Error(Ui_erro):
    def __init__(self, error) -> None:
        self.setupUi(error)
        self.back_button.clicked.connect(self.back)
      
    def back(self):
        screen_error.close()
        second.show()


class Play_error(Ui_play_error):
    def __init__(self, play_erro):
        self.setupUi(play_erro)
        self.back_topage.clicked.connect(self.back_page)

    def back_page(self):
        error_play.close()
        window.show()

             
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    screen = First(window)
    window.show()
    
    second = QtWidgets.QMainWindow()
    second_screen = Second(second)

    book_screen = QtWidgets.QMainWindow()
    screen_book = Screen_Book(book_screen)
    
    mirror_screen = QtWidgets.QMainWindow()
    screen_mirror = Screen_mirror(mirror_screen)
    
    last_tip =  QtWidgets.QMainWindow()
    tip_last = Last_tip(last_tip)
    
    penultimate_screen =  QtWidgets.QMainWindow()
    screen_penultimate = Penultimate_screen(penultimate_screen)
    
    key =  QtWidgets.QMainWindow()
    key_find = Key(key)
    
    final =  QtWidgets.QMainWindow()
    final_true = Final(final)
    
    screen_error = QtWidgets.QMainWindow()
    error_screen = Error(screen_error)

    error_play = QtWidgets.QMainWindow()
    play_error = Play_error(error_play)

    sys.exit(app.exec_())


