#-*- coding : utf-8 -*-
import socket
def serveur(port):
    hote = ''
    connexion_principale = socket.socket(socket.AF_INET,
    socket.SOCK_STREAM)
    connexion_principale.bind((hote, port))
    connexion_principale.listen(5)
    print("Le serveur ecoute  sur le port {}".format(port))
    connexion_avec_client, infos_connexion = connexion_principale.accept()
    msg_recu = b""
    while msg_recu != b"fin":
        msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si lemessage

        print(msg_recu.decode())
        connexion_avec_client.send(b"5 / 5")
    print("Fermeture de la connexion")
    connexion_avec_client.close()
    connexion_principale.close()
    return 1