#-*-coding: utf-8 -*-
# __author__ Gaetan Jonathan

from tkinter import *
import pygame 
import threading, time

pygame.init()

class Intro(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)  # je precise que cette classe est une classe qui est lancé en tant que thread
 

    def run(self):  # la fonction qui va etre lancer en threading
        self.etat = True
        import anim
        self.etat = False



class Interface():
    def __init__(self):
        self.root = Tk()  #  creation de ma fenetre
        self.root.title('QPC SESAME')
        self.root.geometry('1200x600')  # taille de la fenetre 
        self.root.resizable(width=False, height=False)  #  empecher le redimensionnement

    
    def __final__(self):
        self.root.mainloop()  #  lancement de la fenetre


class Sound(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.son = pygame.mixer.Sound("animation.wav")

    def run(self):
        self.son.play()

        

if __name__ =='__main__':
    
    thread1 = Intro()  #  instanciation du classe qui contient le thread
    thread2 = Sound()

    thread1.start()
    thread2.start()

    time.sleep(2)  #  mettre en pause pendant 2s pour assurer que la classe thread demarre

    while thread1.etat : # J'attend que le thread s'arrete
        time.sleep(0.1)

       
    fen = Interface()   #  lanceons now notre fenetre
    fen.__final__()
    