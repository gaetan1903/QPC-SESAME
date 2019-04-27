#-*-coding: utf-8 -*-
# __author__ Gaetan Jonathan

from tkinter import * 
import threading, time


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
        self.root.geometry('1200x600+100+50')  # taille de la fenetre 
        self.root.resizable(width=False, height=False)  #  empecher le redimensionnement
        self.fsociety0 = PhotoImage(file='logo.png')
        self.esti0 = PhotoImage(file='esti.png')
        self.sesame0 = PhotoImage(file='sesame.png')

    def __corps__(self):
        self.eval = Canvas(self.root, bg = 'white', width = 1200, height = 75)
        self.eval.place(relx = -0.001, rely = -0.001)
       
        self.fsociety = self.fsociety0.subsample(4,4)
        self.esti = self.esti0.subsample(10, 10)
        self.sesame = self.sesame0.subsample(20, 20)

        self.eval.create_image(600, 43 , image = self.fsociety)
        self.eval.create_image(60, 37 , image = self.esti)
        self.eval.create_image(1140, 37 , image = self.sesame)

        self.footer = Canvas(self.root, bg = 'teal', width = 1200, height = 50)
        self.footer.place(relx = -0.001, rely = 0.92)

        self.footer.create_text(1120, 25, text = '© Copyright Juin 2019', activefill = 'yellow')
        self.footer.create_text(115, 25, text = '♣ Licence Libre && Open Source', activefill = 'yellow')
        self.footer.create_text(625, 25, text = '☻  ambatoroka.f-society@gmail.com', activefill = 'yellow')

    
    def __final__(self):
        self.root.mainloop()  #  lancement de la fenetre

        

if __name__ == '__main__':
    
    thread1 = Intro()  #  instanciation du classe qui contient le thread
    thread1.start()

    time.sleep(2)  #  mettre en pause pendant 2s pour assurer que la classe thread demarre

    while thread1.etat : # J'attend que le thread s'arrete
        time.sleep(0.1)
       
    fen = Interface()   #  lanceons now notre fenetre
    fen.__corps__()
    fen.__final__()
    
