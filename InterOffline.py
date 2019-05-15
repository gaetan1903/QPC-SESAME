from tkinter import *
import tkinter.messagebox as tkmsg

class InterOflline():
    """
        classe permettant de traiter la fenetre principal du mode de jeu en Offline 
                                                                                    """ 
    def __init__(self):
        self.root = Tk()  #  creation de ma fenetre
        self.root.config(bg='white')
        self.root.title('QPC SESAME: MODE HORS LIGNE')
        self.root.geometry('1200x600+0+0')  # taille de la fenetre 
        #self.root.wm_state(newstate="zoomed")  #  plein ecran windows
        #self.root.resizable(width=False, height=False)


    def menuTop(self):
        self.menubutton = Menu(self.root)
        self.sous_menubutton_1 = Menu(self.menubutton, tearoff =0)
        self.menubutton.add_cascade(label = "Fichier"  , menu = self.sous_menubutton_1)
        self.sous_menubutton_1.add_command(label ="Nouvelle fenetre")
        self.sous_menubutton_1.add_command(label ="Quitter", command = self.confirmQuitter)
        self.root.config(menu = self.menubutton)


    def __corps__(self):
        self.nav = Canvas(self.root, bd = 4, highlightthickness = 1, bg = 'white', width = 1366, height = 25)
        self.nav.place(relx = 0, rely = 0)
        #  self.backbutton = Button(self.root, text = 'RETOUR', bd = 0, command = self.retour).place(relx = 0.93, rely = 0.004)


    def retour(self):
        self.root.destroy()
        self.root.quit()
        


    def confirmQuitter(self):
        self.fermer = tkmsg.askquestion("Confirmer la fermeture!", "Voulez-vous vraiment quitter?")
        if self.fermer == "yes":
            self.root.destroy()
            self.root.quit()


    def __final__(self):
        self.root.mainloop()

    
    def configJeu(self):
        fenfille = Toplevel()



def main():
    fen = InterOflline()
    fen.configJeu()
    fen.__corps__()
    fen.menuTop()
    fen.__final__()
   



main()