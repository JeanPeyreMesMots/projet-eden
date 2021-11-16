#!/usr/bin/python3

import socket
import select

def init():
    l = []
    lx = []
    ly = []

    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(("", 7777))
    s.listen(2)
    l.append(s)
    return l, s
