#-*-coding: utf-8 -*-
# __author__ Gaetan Jonathan

from tkinter import * 
import threading, time
import tkinter.font as tkFont
import tkinter.messagebox as tkmsg


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
        self.root.title('Question Pour un Champion SESAME')
        self.root.geometry('1200x600+100+50')  # taille de la fenetre
        self.root['bg'] = '#032f62'
        self.root.resizable(width=False, height=False)  #  empecher le redimensionnement

        self.helv32 = tkFont.Font(family='Helvetica', size=32, weight='bold')
        self.helv36 = tkFont.Font(family='Arial', size=36, weight='bold')

        self.offline0 = PhotoImage(file='offline.png')
        self.poussoir0 = PhotoImage(file='poussoir.png')
        self.fsociety0 = PhotoImage(file='logo.png')
        self.esti0 = PhotoImage(file='esti.png')
        self.sesame0 = PhotoImage(file='sesame.png')
        self.reseau0 = PhotoImage(file='reseau.png')
        self.projet0 = PhotoImage(file='projet.png')

        self.count = 0
         

    def __corps__(self):
        self.eval = Canvas(self.root, bg = 'white', width = 1200, height = 75)
        self.eval.place(relx = -0.001, rely = -0.001)
       
        self.fsociety = self.fsociety0.subsample(4,4)
        self.esti = self.esti0.subsample(10, 10)
        self.sesame = self.sesame0.subsample(20, 20)
        self.offline = self.offline0.subsample(6, 6)
        self.poussoir = self.poussoir0.subsample(2, 2)
        self.reseau = self.reseau0.subsample(2,2)

        self.eval.create_image(600, 43 , image = self.fsociety)
        self.eval.create_image(60, 37 , image = self.esti)
        self.eval.create_image(1140, 37 , image = self.sesame)

        self.footer = Canvas(self.root, bg = 'teal', width = 1200, height = 50, bd = 0)
        self.footer.place(relx = -0.001, rely = 0.92)

        self.footer.create_text(1120, 25, text = '© Copyright Juin 2019', activefill = 'orange', fill ='yellow')
        self.footer.create_text(115, 25, text = '♣ Licence Libre && Open Source', activefill = 'orange', fill ='yellow')
        self.footer.create_text(620, 25, text = '☻  ambatoroka.f-society@gmail.com', activefill = 'orange', fill ='yellow')

        self.ModeJeuLabel = Label(self.root, text = 'MODE DE JEU', bg ='#032f62', fg = 'white', font = self.helv36).place(relx = 0.36, rely = 0.13)

        self.offlineButton = Button(self.root, bd =0, bg ='#032f62',  image = self.offline, command = self.offlineCommand)
        self.offlineButton.place(relx = 0.03, rely = 0.3)
        self.offlineLabel = Label(self.root, text = 'HORS LIGNE', bg = '#032f62', fg ='white',  font = self.helv32).place(relx = 0.035, rely = 0.75)

        self.poussoirButton = Button(self.root, bd = 0, bg ='#032f62', image = self.poussoir, command = self.poussoirCommand)
        self.poussoirButton.place(relx = 0.41, rely = 0.3)
        self.poussoirLabel = Label(self.root, text = 'POUSSOIR', bg = '#032f62', fg ='white',font = self.helv32).place(relx = 0.41, rely = 0.75)

        self.reseauButton = Button(self.root, bd = 0, bg ='#032f62', image = self.reseau, command = self.reseauCommand)
        self.reseauButton.place(relx = 0.75, rely = 0.3)
        self.reseauLabel = Label(self.root, text = 'EN RESEAU', bg = '#032f62',fg ='white', font = self.helv32).place(relx = 0.755, rely = 0.75)

    def on_Close(self):
            self.count = 0  #  retour au zero du compteur
            self.fen_f1.destroy()


    def offlineCommand(self):
        self.count += 1 

        if self.count <= 1:
            self.fen_f1 = Toplevel(self.root)
            self.fen_f1.title('QPC SESAME')
            self.fen_f1.geometry('400x100')
            self.projet = self.projet0.subsample(6, 6)
            projetImage = Label(self.fen_f1, image = self.projet).place(relx = 0.39, rely = 0.10)

            newButton = Button(self.fen_f1, text = 'Nouveau Projet', activeforeground ='teal')
            newButton.place(relx = 0.05, rely = 0.45)
            openButton = Button(self.fen_f1, text = 'Ouvrir un Projet', activeforeground ='#032f62').place(relx = 0.65, rely = 0.45)
            self.fen_f1.protocol("WM_DELETE_WINDOW", self.on_Close)  #  evenement en cas de fermeture 
            self.fen_f1.mainloop()

        else:
            self.fen_f1.withdraw()  #  cache la fenetre 
            self.fen_f1.deiconify()  #  reaffiche la fenetre

        
        

        """
        fen.root.withdraw()
        fen1 = InterOflline()
        fen1.menuTop()
        fen1.__corps__()
        fen1.__final__()
        """

    
    def poussoirCommand(self):
        fen.root.destroy()
        fen2 = InterPoussoir()
        fen2.menuTop()
        fen2.__final__()

    
    def reseauCommand(self):
        fen.root.destroy()
        fen3 = InterReseau()
        fen3.__final__()
    

    def __final__(self):
        self.root.mainloop()  #  lancement de la fenetre



class InterOflline():
    def __init__(self):
        self.root = Tk()  #  creation de ma fenetre
        self.root.title('QPC SESAME: MODE HORS LIGNE')
        self.root.geometry('1200x600+100+50')  # taille de la fenetre 
        self.root.resizable(width=False, height=False)

        self.backImage0 = PhotoImage(file='retour.png')


    def menuTop(self):
        self.menubutton = Menu(self.root)
        self.sous_menubutton_1 = Menu(self.menubutton, tearoff =0)
        self.menubutton.add_cascade(label = "Fichier"  , menu = self.sous_menubutton_1)
        self.sous_menubutton_1.add_command(label ="Nouvelle fenetre")
        self.sous_menubutton_1.add_command(label ="Quitter", command = self.confirmQuitter)
        self.root.config(menu = self.menubutton)


    def __corps__(self):
        self.nav = Canvas(self.root, bg = '#032f62', width = 1200, height = 43, bd = 0).place(relx = - 0.001, rely = - 0.015)
        self.backImage = self.backImage0.subsample(8,8)
        self.backbutton = Button(self.root, text = 'RETOUR', bd = 0, bg = 'grey', command = self.retour).place(relx = 0.93, rely = 0.004)

    def retour(self):
        fen.root.deiconify()
        self.root.destroy()


    def confirmQuitter(self):
        self.fermer = tkmsg.askquestion("Confirmer la fermeture!", "Voulez-vous vraiment quitter?")
        if self.fermer == "yes":
            self.root.destroy()


    def __final__(self):
        self.root.mainloop()


class InterPoussoir():
    def __init__(self):
        self.root = Tk()  #  creation de ma fenetre
        self.root.title('QPC SESAME: MODE POUSSOIR')
        self.root.geometry('1200x600+100+50')  # taille de la fenetre 
        self.root.resizable(width=False, height=False)


    def menuTop(self):
        self.menubutton = Menu(self.root)
        self.sous_menubutton_1 = Menu(self.menubutton, tearoff =0)
        self.menubutton.add_cascade(label = "Fichier"  , menu = self.sous_menubutton_1)
        self.sous_menubutton_1.add_command(label ="Nouvelle fenetre")
        self.sous_menubutton_1.add_command(label ="Quitter", command = self.ConfirmeQuitter)
        self.root.config(menu = self.menubutton)


    def confirmQuitter(self):
        self.fermer = tkmsg.askquestion("Confirmer la fermeture!", "Voulez-vous vraiment quitter?")
        if self.fermer == "yes":
            self.root.quit()



    def __final__(self):
        self.root.mainloop()



class InterReseau():
    def __init__(self):
        self.root = Tk()  #  creation de ma fenetre
        self.root.title('Question Pour un Champion SESAME')
        self.root.geometry('1200x600+100+50')  # taille de la fenetre 
        self.root.resizable(width=False, height=False)


    def __final__(self):
        self.root.mainloop()



if __name__ == '__main__':
    
    thread1 = Intro()  #  instanciation du classe qui contient le thread
    thread1.start()

    time.sleep(2)  #  mettre en pause pendant 2s pour assurer que la classe thread demarre

    while thread1.etat : # J'attend que le thread s'arrete
        time.sleep(0.1)
       
    fen = Interface()   #  lanceons now notre fenetre
    fen.__corps__()
    fen.__final__()
    
