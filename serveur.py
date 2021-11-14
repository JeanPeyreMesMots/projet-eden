#!/usr/bin/python3

import socket, threading, select

# Sockets lists
liste = []

def socketServeur():
    # Socket serveur
    mySocket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
    mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mySocket.bind(("", 7777))
    mySocket.listen(1)
    
    # Ajout de la socket à la liste
    liste.append(mySocket)
    return liste, mySocket

def discoverClients(liste, mySocket):
    # Prendre la liste vide
        # avec la socket serveur
        readl, writel, errorl = select.select(liste, [], [])

        # Pour chaque client connecté
        for i in readl:
            # Si socket serveur
            if(i==mySocket):
                socketCliente, addrS = mySocket.accept()
                # Extrait de l'adresse et port
                adrressClient = socketCliente.getpeername()
                (ADRESSE, port, zero1, zero2) = adrressClient
                # Affichage
                print("Client connected : ", ADRESSE + ":" + str(port))
                # Ajout de la socket à la liste
                liste.append(socketCliente)

            else:
                # Sinon, traitement des clients
                msg = i.recv(1500)
                decoded = msg.decode("utf-8")    
                # Si message vide
                if len(decoded) == 0:
                    print("Client disconnected: ", ADRESSE + ":" + str(port))
                    i.close()
                    liste.remove(i)

        return liste