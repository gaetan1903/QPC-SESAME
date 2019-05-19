#-*-coding: Utf-8 -*-
# __author__: Gaetan Jonathan BAKARY

from tkinter.filedialog import * 

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