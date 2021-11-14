import socket, threading, select

# Sockets lists
l = []
emptyL = []
emptyL2 = []

#def testPrint():
#    print("Commence à me parler poliment...")

def connection():
    # Socket serveur
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 7777))
    s.listen(1)

    # Ajout de la socket à la liste
    l.append(s)
    return l, s

    """
    # Boucle infinie
    while True:
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
        """