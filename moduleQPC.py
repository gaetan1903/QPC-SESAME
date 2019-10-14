#-*-coding: Utf-8 -*-
# __author__: Gaetan Jonathan BAKARY

from tkinter.filedialog import *
import threading, playsound 

"""
    Classe permettant de classer les petits fonction
        que l'on aurait besoin durant le codage pour but optimiser le code 
                                                                            """

def recupfichier(extension):
    """
        fonction permettant de retourner d'ouvrir 
            l'explorer et retourner le chemin du fichier selectionner 
                                                                        """
    return askopenfilename(filetypes=[(f".{extension}", f"*.{extension}")])


def saveFichier(defaultextension, initialfile, title):
    """ 
        fonction permettant d'ouvrir l explorer et de creer
            le fichier et l emplacement pour le  sauvegarder
                                                                """
    return asksaveasfilename(defaultextension = defaultextension, initialfile = initialfile, title = title)


class LancerSound(threading.Thread):
    def __init__(self, son):
        threading.Thread.__init__(self)
        self.son = son

    def run(self):
        playsound.playsound(self.son)


def lancerson(son):
    p = LancerSound(son)
    p.start()


def create_server(port, nbr_joueur):
    """
        fonction permettant
            de creer un serveur de jeu 
                                        """
    connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_principale.bind(('', port))
    connexion_principale.listen(nbr_joueur)