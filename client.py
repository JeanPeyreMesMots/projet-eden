#!/usr/bin/python3

import socket
import serveur
import select

BUFFSIZE = 1024

def connect(host, port):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if(clientSocket.connect((host, port))):
        print("Connected")
    data = clientSocket.recv(BUFFSIZE)