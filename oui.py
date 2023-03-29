# Librairie
import socket
# Création d'une socket pour communiquer sur un réseau
# informatique en TCP
ma_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connexion au serveur
ma_socket.connect(("10.229.253.48", 4711))
# Préparation et envoi de la requête selon le protocole MCPI
requete = "chat.post(Pourquoi la petite fille tombe de la balançoire ? Parce qu'elle n'a pas de bras)\n"
ma_socket.send(requete.encode())
# Déconnexion du serveur
ma_socket.close()