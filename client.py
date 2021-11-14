import serveur, select

def discoverClients(l, s):
    # Prendre la liste vide
        # avec la socket serveur
        readl, writel, errorl = select.select(l+[s], [], [])

        # Pour chaque client connecté
        for i in readl:
            # Si socket serveur
            if(i==s):
                newSock, addrS = s.accept()
                # Extrait de l'adresse et port
                adrressClient = newSock.getpeername()
                (ADRESSE, port, zero1, zero2) = adrressClient
                # Affichage
                print("Client connected : ", ADRESSE + ":" + str(port))
                # Ajout de la socket à la liste
                l.append(newSock)