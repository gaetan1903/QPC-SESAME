#-*-coding: Utf-8 -*-
# __author__: Gaetan Jonathan BAKARY

from tkinter import *
import tkinter.messagebox as tkmsg
from Interface import Interface


class InterJeu:
    def __init__(self):
        """
            class mere d'une ouverture de fenetre de jeu 
                dans le but de ne pas reécrire chque init pour chaque code
                                                                            """
        self.root = Tk()  #  creation de ma fenetre
        self.root.config(bg='white')  #  fond blanc 
        self.root.geometry('1200x600+0+0')  # taille de la fenetre 
        self.root.wm_state(newstate="zoomed")  #  plein ecran windows
        self.root.resizable(width=False, height=False)


class InterOflline(InterJeu):
    """
        classe permettant de traiter la fenetre principal du mode de jeu en Offline 
                                                                                    """ 
    def __init__(self):
        InterJeu.__init__(self)
        self.root.title('QPC SESAME: MODE HORS LIGNE')
        x = Interface.getdict()
        print(x)
        

    def menuTop(self):
        self.menubutton = Menu(self.root)
        self.sous_menubutton_1 = Menu(self.menubutton, tearoff =0)
        self.sous_menubutton_2 = Menu(self.menubutton, tearoff = 0)
        self.menubutton.add_cascade(label = "Fichier"  , menu = self.sous_menubutton_1)
        self.menubutton.add_cascade(label = "Aide"  , menu = self.sous_menubutton_2)
        self.sous_menubutton_1.add_command(label ="Nouvelle fenetre")
        self.sous_menubutton_1.add_command(label ="Ouvrir un autre projet")
        self.sous_menubutton_1.add_command(label ="Quitter", command = self.confirmQuitter)
        self.root.config(menu = self.menubutton)


    def __corps__(self):
        self.nav = Canvas(self.root, bd = 4, highlightthickness = 1, bg = 'white', width = 1366, height = 25)
        self.nav.place(relx = 0, rely = 0)


    def retour(self):
        self.root.destroy()
        self.root.quit()
        

    def confirmQuitter(self):
        self.fermer = tkmsg.askquestion("Confirmer la fermeture!", "Voulez-vous vraiment quitter?")
        if self.fermer == "yes":
            self.root.quit()


    def __final__(self):
        self.root.mainloop()




class InterPoussoir(InterJeu):
    def __init__(self):
        InterJeu.__init__(self)
        self.root.title('QPC SESAME: MODE POUSSOIR')






def pouss():
    pass
   