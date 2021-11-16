#!/usr/bin/python3

import select
import pygame

def init(l, s):
    ll, _, _ = select.select(l, [], [])
    #print("while")
    for soc in ll:
        #print("for")
        if (soc == s):
            #print("if")
            cn, addr = s.accept()
            l.append(cn)
    return l

def lecture(soc, s):
        if (soc != s):
            e = pygame.event.wait()
            return e
