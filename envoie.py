#!/usr/bin/python3

import pygame
import sys, socket

def envoie(soc, requete):
    for nb in requete:
        data = nb.encode("utf-8")
        soc.sendall(data)
