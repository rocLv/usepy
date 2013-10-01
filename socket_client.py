#coding=utf-8
#!/usr/bin/env python

# socket client

import socket

HOST = 'localhost'
PORT = 2345
BUFFSIZE = 1024
ADDR = (HOST, PORT)

def tcpSocket():
    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    tcpCliSock.connect(ADDR)
    
    while True:
        data = raw_input('> ')
        if not data:
            break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFFSIZE)
        if not data:
            break
        print data
    
    tcpCliSock.close()

def udpSocket():
    udpCliSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # redefined ?
    HOST = 'localhost'
    PORT = 2345
    ADDR = (HOST, PORT)

    while True:
        data = raw_input('> ')
        if not data:
            break
        udpCliSock.sendto(data,ADDR) # what the hell 'undefined ADDR' ?!
        data, ADDR = udpCliSock.recvfrom(BUFFSIZE)
        if not data:
            break
        print data

    udpCliSock.close()


print '--- Socket Client ---'
print ADDR
udpSocket()




