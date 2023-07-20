import pygame
import time
from threading import Thread

def music_computer():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('musicas/computer.mp3')
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.mixer.music.stop()        
           
def thread_computer():
    tempo = Thread(target=music_computer)
    tempo.start()
    
def music_book():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('musicas/livro_musica.mp3')
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.mixer.music.stop()

def thread_book():
    tempo = Thread(target=music_book)
    tempo.start()
    
    
def music_error():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('musicas/Som de erro.mp3')
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.mixer.music.stop()
 
def thread_error():
    tempo = Thread(target=music_error)
    tempo.start()
    
def music_rigth():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('musicas/Som de resposta certa.mp3')
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.mixer.music.stop()
        
def thread_right():
    tempo = Thread(target=music_rigth)
    tempo.start()
    
def music_playground():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('musicas/criancas2.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.stop()
    
def thread_playground():
    tempo = Thread(target=music_playground)
    tempo.start()
    
def user_write():
    thread_error()
    time.sleep(1)
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('musicas/computer.mp3')
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.mixer.music.stop()
    
def thread_user():
    tempo = Thread(target=user_write)
    tempo.start()

def music_idea():
    pygame.mixer.init()
    pygame.mixer_music.load("musicas/ideia.mp3")
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.mixer.music.stop()

def thread_idea():
    tempo = Thread(target=music_idea)
    tempo.start()

        
    
    
        