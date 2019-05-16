#-*-coding: Utf-8 -*-
# __author__: Gaetan Jonathan

from tkinter import * 
import threading, time
import tkinter.font as tkFont
import tkinter.messagebox as tkmsg
from tkinter.filedialog import *
import json  #  load charger en dict , loads charger dict en str, dumps dict en json

i = j = 0  #  compteur utile

class Interface():
    def __init__(self):
        """
            Constructeur de la classe Interface   
                                                    """
        self.root = Tk()  #  creation de ma fenetre
        self.root.title('Menu Principale')
        self.root.geometry('1200x600+100+50')  # taille de la fenetre + position
        self.root['bg'] = 'white'  # couleur du fond 
        self.root.resizable(width=False, height=False)  #  empecher le redimensionnement
        #  ci dessous est varible contenant des fonts
        self.helv32 = tkFont.Font(family='Helvetica', size=32, weight='bold')
        self.helv36 = tkFont.Font(family='Arial', size=36, weight='bold')
        self.arial24 = tkFont.Font(family='Arial', size=22, weight='bold')
        self.verdana30 = tkFont.Font(family='Verdana', size = 30, weight = 'bold')
        self.arialinfo0 = tkFont.Font(family='Arial', size=18)
        self.arialinfo = tkFont.Font(family='Arial', size=16)
        self.arialinfo14 = tkFont.Font(family='Arial', size=14)
        #  ci dessous est variable contenant les images en taille initiale
        self.offline0 = PhotoImage(file='offline.png')
        self.poussoir0 = PhotoImage(file='poussoir.png')
        self.fsociety0 = PhotoImage(file='logo.png')
        self.esti0 = PhotoImage(file='esti.png')
        self.backImage0 = PhotoImage(file='')
        self.sesame0 = PhotoImage(file='sesame.png')
        self.reseau0 = PhotoImage(file='reseau.png')
        self.projet0 = PhotoImage(file='projet.png')
        self.setting0 = PhotoImage(file='settings.png')

        self.count = 0  #  initialisation d'un compteur
         

    def __corps__(self):
        """
            Methode contenant le corps de l'Interface principal
                                                                    """
        #  creation et positionnement d'un canvas
        self.eval = Canvas(self.root, bg = 'white', width = 1200, height = 75)
        self.eval.place(relx = -0.001, rely = -0.001)

        self.eval.create_text(602, 38 , text = 'Question Pour un Champion', font = self.verdana30, fill = 'teal')  #  creation du titre en tant que text
        self.fsociety = self.fsociety0.subsample(8, 8)
        self.sesame = self.sesame0.subsample(20, 20)  #  image redimensionner 

        self.eval.create_image(90, 40 , image = self.fsociety) 
        self.eval.create_image(1140, 37 , image = self.sesame)  #  nametraka image a un position 

        self.footer = Canvas(self.root, bg = 'teal', width = 1202, height = 50, bd = 0, highlightthickness = 0)  #  canvas en bas 
        self.footer.place(relx = -0.001, rely = 0.92)  #  sa position 
        # ci dessous les elements a placé sur le canvas
        self.footer.create_text(1120, 25, text = '© Copyright Juin 2019', activefill = 'orange', fill ='yellow')
        self.footer.create_text(105, 25, text = '♣ Licence Libre & Open Source ♣', activefill = 'orange', fill ='yellow')
        self.footer.create_text(600, 25, text = '☻ ambatoroka.fsociety@gmail.com ☻', activefill = 'orange', fill ='yellow')

        self.menuJeu = Canvas(self.root, bg = 'teal', highlightthickness = 0, width = 1202, height = 65)
        self.menuJeu.place(relx = - 0.001, rely = 0.1278)  #  canvas pour les choix de mode de jeu 

        #  Ci dessous la creation du bouton mode offline avec ses comportements
        self.offlineButton = Button(self.root, bd = 0, fg = 'yellow', cursor ='hand2', relief = 'groove',  bg = 'teal', activeforeground = 'yellow', activebackground = 'teal', text = "Mode Offline",  font = self.arial24, command = self.offlineCommand)
        self.offlineButton.place(relx = 0.005, rely = 0.13)
        self.offlineButton.bind("<Enter>", self.offlinemouseOverEnter)  # evenement survole le souris lance la fonction precisé
        self.offlineButton.bind("<Leave>", self.offlinemouseOverLeave)  #  evenement contraire du celle du dessus
    

    def fen_f1Close(self):
            self.count = 0  #  retour au zero du compteur
            self.fen_f1.destroy()


    def openProject(self):
        self.fen_f1.destroy()
        self.count = 0
        self.file = askopenfilename(filetypes=[(".qpc","*.qpc")])

        if self.file is not '':

            f = open(self.file, 'r')
            self.continuer = False
            for x in f:
                if x[0] == '{':
                    self.continuer = True
                    
                break
            
            if self.continuer:
                self.root.withdraw()
                import InterOffline
                self.root.deiconify()

            else:  #  mauvais fichier 
                self.root.withdraw()
                self.root.deiconify()
                tkmsg.showwarning('Fichier non valide', 'Attention, veuillez selectionner le bon fichier...')
        
        else:   #  cas d une annulation
            self.root.withdraw()
            self.root.deiconify()

    
    def newProject(self):
        self.count = 0
        self.dict = {}
        self.dict['Question1'] = []
        self.dict['Reponse1'] = []
        #  une petite formatage de texte
        self.dict['Question2'] = []
        self.dict['Reponse2'] = []
        #  une petite formatage de texte
        self.dict['Question3'] = []
        self.dict['Reponse3'] = []

        self.fen_f1.destroy()
        self.fen_ques1 = Toplevel(self.root)
        self.fen_ques1.title('QPC SESAME: Question')
        self.fen_ques1['bg'] = 'white'
        self.fen_ques1.geometry('700x500+400+100')
        self.fen_ques1.protocol("WM_DELETE_WINDOW", self.fen_quesClose)

        self.fen_ques1Topnav = Canvas(self.fen_ques1, width = 705, height = 35, bg = 'white')
        self.fen_ques1Aftnav = Canvas(self.fen_ques1, width = 705, height = 35, bg = 'teal', highlightthickness = 0)
        self.fen_ques1Topnav.place(relx = -0.00001, rely = 0.01)
        self.fen_ques1Aftnav.place(relx = -0.00001, rely = 0.08)

        self.etiquette = ['Niveau 1', 'Niveau 2', 'Niveau 3']
        self.values = [1 , 2 , 3]
        self.niveau = IntVar()
        for i in range(3):
            self.Rniveau = Radiobutton(self.fen_ques1, variable = self.niveau, text = self.etiquette[i], value = self.values[i], font = self.arialinfo14)
            self.Rniveau.place(relx =(0.1+(i*0.3)), rely = 0.2)
        del i  
        self.champQuestion = Text(self.fen_ques1, height = 6, width = 70, bg = 'lightgray')
        self.champQuestion.place(relx = 0.1, rely = 0.35)
        self.champQuestion.insert('1.0', "Enter la question...")
        self.champQuestion.bind("<Button-1>", self.champQuestionOverEnter)

        self.reponse = StringVar()
        self.reponse.set('Entrer la réponse... ')
        self.champReponse = Entry(self.fen_ques1,  textvariable = self.reponse, width = 50, bg = 'lightgray', font = self.arialinfo14, fg = '#333')
        self.champReponse.place(relx = 0.1, rely = 0.6)
        self.champReponse.bind("<Button-1>", self.champReponseOverEnter)

        self.enrButton = Button(self.fen_ques1, text = 'Enregistrer', font = self.arialinfo, command = self.enregistrer)
        self.enrButton.place(relx = 0.1, rely = 0.7)

        self.verButton = Button(self.fen_ques1, text = 'Verifier', font = self.arialinfo, command = self.verifier)
        self.verButton.place(relx = 0.77, rely = 0.7)

        self.fen_ques1Topnav.create_text(330, 18, text = 'Projet Questions', font = self.arialinfo14, fill = 'teal')

        self.setting = self.setting0.subsample(2, 2)

        self.niveau1Set = Button(self.fen_ques1, image = self.setting, highlightthickness = 0 , bg = 'white', bd = 0, command = self.changeValue1)
        self.niveau1Set.place(relx = 0.25,rely = 0.21)

        self.niveau2Set = Button(self.fen_ques1, image = self.setting, highlightthickness = 0 , bg = 'white', bd = 0, command = self.changeValue2)
        self.niveau2Set.place(relx = 0.55,rely = 0.21)

        self.niveau3Set = Button(self.fen_ques1, image = self.setting, highlightthickness = 0 , bg = 'white', bd = 0, command = self.changevalue3)
        self.niveau3Set.place(relx = 0.85,rely = 0.21)

        self.termButton = Button(self.fen_ques1, text = 'TERMINER',font = self.arialinfo14, fg = 'teal', command = self.terminer)
        self.termButton.place(relx = 0.42, rely = 0.85)


    def changeValue1(self):
        self.fenVal1 = Toplevel(self.fen_ques1)
        self.fenVal1.title("Point d'incrémentation")
        self.fenVal1.geometry('+500+250')
        self.valeur1 = IntVar()
        label = Label(self.fenVal1, text = 'Entrer le nombre de point du question "Niveau 1" ').pack()
        entre = Entry(self.fenVal1, textvariable = self.valeur1)
        self.valeur1.set(self.values[0])
        entre.pack()
        boutton = Button(self.fenVal1, text = 'Valider', width = 20, command = self.getValue1).pack()

    
    def changeValue2(self):
        self.fenVal2 = Toplevel(self.fen_ques1)
        self.fenVal2.title("Point d'incrémentation")
        self.fenVal2.geometry('+550+250')
        self.valeur2 = IntVar()
        label = Label(self.fenVal2, text = 'Entrer le nombre de point du question "Niveau 2" ').pack()
        entre = Entry(self.fenVal2, textvariable = self.valeur2)
        self.valeur2.set(self.values[1])
        entre.pack()
        boutton = Button(self.fenVal2, text = 'Valider', width = 20, command = self.getValue2).pack()
    
    
    def changevalue3(self):
        self.fenVal3 = Toplevel(self.fen_ques1)
        self.fenVal3.title("Point d'incrémentation")
        self.fenVal3.geometry('+550+250')
        self.valeur3 = IntVar()
        label = Label(self.fenVal3, text = 'Entrer le nombre de point du question "Niveau 3" ').pack()
        entre = Entry(self.fenVal3, textvariable = self.valeur3)
        self.valeur3.set(self.values[2])
        entre.pack()
        boutton = Button(self.fenVal3, text = 'Valider', width = 20, command = self.getValue3).pack()


    def getValue1(self):
        self.values[0] = self.valeur1.get()
        self.Rniveau.destroy()
        self.fenVal1.destroy()
        self.valeur1.set(self.values[0])
        for i in range(3):
            self.Rniveau = Radiobutton(self.fen_ques1, variable = self.niveau, text = self.etiquette[i], value = self.values[i], font = self.arialinfo14)
            self.Rniveau.place(relx =(0.1+(i*0.3)), rely = 0.2)

    
    def getValue2(self):
        self.values[1] = self.valeur2.get()
        self.Rniveau.destroy()
        self.fenVal2.destroy()
        self.valeur2.set(self.values[1])
        for i in range(3):
            self.Rniveau = Radiobutton(self.fen_ques1, variable = self.niveau, text = self.etiquette[i], value = self.values[i], font = self.arialinfo14)
            self.Rniveau.place(relx =(0.1+(i*0.3)), rely = 0.2)


    def getValue3(self):
        self.values[2] = self.valeur3.get()
        self.Rniveau.destroy()
        self.fenVal3.destroy()
        self.valeur3.set(self.values[2])
        for i in range(3):
            self.Rniveau = Radiobutton(self.fen_ques1, variable = self.niveau, text = self.etiquette[i], value = self.values[i], font = self.arialinfo14)
            self.Rniveau.place(relx =(0.1+(i*0.3)), rely = 0.2)

    
    def enregistrer(self):
        """
            une fonction permettant d enregistrer temporairement 
                dans la RAM , les questions et reponses entrées dans le projet
                                                                                """
        effacer = True 
        textget = self.champQuestion.get('1.0','10.0')  #  recupere l entré du champ question 

        if self.niveau.get() == self.values[0]:
            self.dict['Question1'].append([textget, len(textget.strip())])
            self.dict['Reponse1'].append([self.reponse.get().strip(), self.niveau.get()])

        elif self.niveau.get() == self.values[1]:
            self.dict['Question2'].append([textget, len(textget.strip())])
            self.dict['Reponse2'].append([self.reponse.get().strip(), self.niveau.get()])

        elif self.niveau.get() == self.values[2]:
            self.dict['Question3'].append([textget, len(textget.strip())])
            self.dict['Reponse3'].append([self.reponse.get().strip(), self.niveau.get()])

        else:
            tkmsg.showwarning('Aucun niveau selectionné', "Attention,\nIl est impératif de selectionner le niveau de cette question")
            self.fen_ques1.withdraw()
            self.fen_ques1.deiconify()
            effacer = False

        if effacer:
            self.reponse.set('')  #  vider le champ
            self.champQuestion.delete('1.0', '10.0')  #  vider le champ

    
    def verifier(self):
        """ 
            fonction permettant de verifier tous les questions
                 avant de terminer pour but d'eviter toute heure durant le jeu
                                                                                """
        self.fen_ver = Toplevel(self.fen_ques1)  #  creation d une fenetre fille 
        self.fen_ver.title('Verification')  #  titre de cette nouvelle fenetre
        self.qrp = StringVar()  #  variable contenant le retour et l entré du liste
        #  methode pour entrer les questions et reponses dans des listes
        q1 = []  #  initialisation d'une liste contenant les questions de types niveau 1 
        for x in self.dict['Question1']:
            q1.append(x[0].replace('\n', ''))  #  ajout des questions de niveau1 dans la liste 
        r1 = []  #  initialisation d'une liste contenant les reponses de types niveau 1  
        for x in self.dict['Reponse1']:
            r1.append((x[0], x[1]))  #  ajout des reponses de niveau 1 dans la liste
        #  même technique que dessus 
        q2 = []
        for x in self.dict['Question2']:
            q2.append(x[0].replace('\n', ''))
        r2= []
        for x in self.dict['Reponse2']:
            r2.append((x[0], x[1]))
        
        q3 = []
        for x in self.dict['Question3']:
            q3.append(x[0].replace('\n', ''))
        r3 = []
        for x in self.dict['Reponse3']:
            r3.append((x[0], x[1]))
        #  ajout des questions et reponses dans une seule variable  et formatage du texte
        tmp = []  #  variable temporaire contenant l ensembles des choses a afficher
        #  pour le niveau  1
        i = 1
        for x in range(1, len(self.dict['Question1']) + 1):
            tmp.append(f"I-{i}) {q1[x-1]}")
            tmp.append(f"--> {r1[x-1][0]}  _*_  {r1[x-1][1]} points")
            tmp.append([])
            i += 1
        #  pour le niveau 2
        i = 1
        for x in range(1, len(self.dict['Question2']) + 1):
            tmp.append(f"II-{i}) {q2[x-1]}")
            tmp.append(f"--> {r2[x-1][0]}  _*_  {r2[x-1][1]} points")
            tmp.append([])
            i += 1
        #  pour le niveau 3
        i =  1
        for x in range(1, len(self.dict['Question3']) + 1):
            tmp.append(f"III-{i}) {q3[x-1]}")
            tmp.append(f"--> {r3[x-1][0]}  _*_  {r3[x-1][1]} points")
            tmp.append([])
            i += 1

        self.qrp.set(tmp)  #  insertion dans la liste  
        #  Mise en place des scrollbar pour les longs textes
        yDefilB = Scrollbar(self.fen_ver, orient='vertical')
        yDefilB.grid(row=0, column=1, sticky='ns')
        xDefilB = Scrollbar(self.fen_ver, orient='horizontal')
        xDefilB.grid(row=1, column=0, sticky='ew')
        #  creation de la liste 
        self.listes = Listbox(self.fen_ver, xscrollcommand = xDefilB.set,  yscrollcommand = yDefilB.set, listvariable = self.qrp, width = 100, height = 20, activestyle = 'dotbox', selectforeground = 'yellow')
        self.listes.grid(row=0, column=0, sticky='nsew')  # positionnement dans la fenetre
        #  les actions des scrollbar 
        xDefilB['command'] = self.listes.xview  
        yDefilB['command'] = self.listes.yview
        #  evenement a un clique droite de la souris
        self.listes.bind('<Button-3>', self.verifConfig)
        self.listes.bind('<Button-1>', self.clickclose)


    def clickclose(self, event):
        try:
            self.option.destroy()
        except:
            pass


    def terminer(self):
        #  ouverture de l'explorateur pour la sauvegarde
        self.file = asksaveasfilename(defaultextension = '.qpc', initialfile = 'project1.qpc', title = 'Sauvegarde du projet')
        #  gestion des erreurs par des conditions
        if self.file is not '':  #  cas d une non  annulation 
            with open(self.file, 'w', encoding = 'utf8') as json_data:  #  ouvrir le fichier creer en mode ecriture 
                json.dump(self.dict, json_data, indent = 4, ensure_ascii = False)  #  parse dans le fichier creer le  dictionnaire des questions 

            self.fen_ques1.destroy()
            self.root.withdraw()
            import InterOffline
            self.root.deiconify()
        
        else:
            self.fen_ques1.withdraw()
            self.fen_ques1.deiconify()


    def verifConfig(self, event):
        """
            fonction lancer a partir d un evenement
                de clique droite de la souris qui a pour but 
                    de modifier ou de suprimé une question ou une une reponse
                                                                                """
        try:
            int(self.listes.curselection()[0])

        except:
            pass 

        else:
            self.option = Frame(self.fen_ver, cursor = 'hand2', bd = 5, highlightcolor = 'orange', highlightthickness = 2, bg ='teal')
            pointX1 = self.fen_ver.winfo_pointerx()
            pointX0 = self.fen_ver.winfo_x() 
            pointY1 = self.fen_ver.winfo_pointery()
            pointY0 = self.fen_ver.winfo_y() + 10

            self.mod = Canvas(self.option, bg = 'teal', width = 60, height = 25, bd = 0 , highlightthickness = 0)
            self.mod.create_text(30, 10 , text = 'Modifier', fill = 'yellow', activefill = 'orange')
            self.mod.pack()
        
            self.eff = Canvas(self.option, bg = 'teal', width = 60 , height = 25, bd = 0 , highlightthickness = 0)
            self.eff.create_text(30, 12 , text = 'Supprimer', fill = 'yellow', activefill = 'orange')
            self.eff.pack()

            self.mod.create_line(0, 24, 60, 24, fill = 'white', width = 2)
            self.option.place(x = pointX1 - pointX0, y = pointY1 - pointY0)
            
            self.mod.bind('<Button-1>', self.modverifier)
            self.eff.bind('<Button-1>', self.effverifier)


    def modverifier(self, event):
        self.option.destroy()


    def effverifier(self, event):
          self.option.destroy()


    def fen_quesClose(self):
        global i
        global j
        i = j = 0
        self.fen_ques1.destroy()


    def champReponseOverEnter(self, event):
        #  fonction permettant de efface le texte en premier entrer
        global i
        if i == 0:
            self.reponse.set('')
        else: 
            pass
        i += 1

    def champQuestionOverEnter(self, event):
        #  fonction permettant de efface le texte en premier entrer
        global j
        if j == 0:
            self.champQuestion.delete('1.0', '1.20')
        else: 
            pass
        j += 1

    
    def offlinemouseOverEnter(self, event):
        self.canvasLink = Canvas(self.root, bg ='teal', width = 251 , height = 5, bd = 0, highlightthickness = 0)
        self.canvasLink.place(relx = 0.005 , rely = 0.2275)
        self.canvasLink.create_rectangle(0, 0, 200 ,5, width = 0,  fill = 'yellow', outline = 'yellow')

        self.canvasInfo = Canvas(self.root, bg ='teal', width = 1000, height = 375)
        self.canvasInfo.place(relx = 0.07, rely = 0.27)

        self.canvasInfo.create_text(500, 20, text = 'Jouer les questions en Mode Oflline? ', font = self.arialinfo0, fill = 'yellow')
        self.canvasInfo.create_text(150, 75, text = " ◊ Unique Ordinateur utilisé ◊ ", font = self.arialinfo, fill = 'white')
        self.canvasInfo.create_text(500, 325, text = " ◊ Incrementation manuel des scores ◊ ", font = self.arialinfo, fill = 'white')
        self.canvasInfo.create_text(850, 75, text = " ◊ Aucun ressource reseau ◊ ", font = self.arialinfo, fill = 'white')
        self.offline = self.offline0.subsample(6,6)
        self.canvasInfo.create_image(500, 175, image =self.offline )


    def offlinemouseOverLeave(self, event):
        self.canvasInfo.destroy()
        self.canvasLink.destroy()


    def offlineCommand(self):
        self.count += 1 

        if self.count <= 1:
            self.fen_f1 = Toplevel(self.root)
            self.fen_f1.title('QPC SESAME')
            self.fen_f1.geometry('400x100')
            self.projet = self.projet0.subsample(6, 6)
            projetImage = Label(self.fen_f1, image = self.projet).place(relx = 0.35, rely = 0.10)

            newButton = Button(self.fen_f1, text = 'Nouveau Projet', activeforeground ='teal', command = self.newProject)
            newButton.place(relx = 0.05, rely = 0.45)
            openButton = Button(self.fen_f1, text = 'Ouvrir un Projet', activeforeground ='#032f62', command = self.openProject).place(relx = 0.65, rely = 0.45)
            self.fen_f1.protocol("WM_DELETE_WINDOW", self.fen_f1Close)  #  evenement en cas de fermeture 
            self.fen_f1.mainloop()

        else:
            self.fen_f1.withdraw()  #  cache la fenetre 
            self.fen_f1.deiconify()  #  reaffiche la fenetre


#  *********************************************************************************************************************************
    
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



if __name__ == '__main__':   
    fen = Interface()   #  lanceons now notre fenetre
    fen.__corps__()
    fen.__final__()
    
