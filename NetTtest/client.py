# -*- coding : utf-8 -*-
import socket
def client():

    hote = "localhost"
    port = 12802
    connexion_avec_serveur = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connexion_avec_serveur.connect((hote, port))
    print("Connexion etablie avec le serveur sur le port{}".format(port))
    msg_a_envoyer = b""
    i = 0
    while msg_a_envoyer != b"fin":
        msg_a_envoyer = input(">> ")
    # Peut planter si vous tapez des caracteres speciaux
        msg_a_envoyer = msg_a_envoyer.encode()
    # On envoie le message
        connexion_avec_serveur.send(msg_a_envoyer)
        i += 1
        if (i >= 5):
            msg_recu = connexion_avec_serveur.recv(1024)
            print(msg_recu.decode()) # La encore, peut planter s'il y a desaccents
            i = 0
    print("Fermeture de la connexion")
    connexion_avec_serveur.close()
    return 1