#coding=utf-8

#!/usr/bin/env python

# socket server

import socket
import time

HOST = ''
PORT = 2345
BUFFSIZE = 1024
ADDR = (HOST, PORT)

def tcpSocket():
    tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)
    
    try:
        while True:
            print ' waiting form connection ...'
            tcpCliSock, addr = tcpSerSock.accept()
            print ' ... connected from : ',addr 
        
            while True:
                data = tcpCliSock.recv(BUFFSIZE)
                if not data:
                    break
                print ' ... recv: ',data
                tcpCliSock.send('[%s] %s' % (time.ctime(), data))
            tcpCliSock.close()
    except EOFError, e:
        print e
    except KeyboardInterrupt, e:
        print e
    finally:
        tcpSerSock.close()

def udpSocket():
    udpSerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpSerSock.bind(ADDR)

    while True:
        print ' waiting for message ...'
        data, addr = udpSerSock.recvfrom(BUFFSIZE)
        print '->> recv: %s ,add: %s ' % (data,addr)
        udpSerSock.sendto('[%s] %s ' % (time.ctime(), data), addr )

    udpSerSock.close()

print '--- Socket Server ---'
udpSocket()
