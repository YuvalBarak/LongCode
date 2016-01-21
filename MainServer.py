from Classes import *
import socket
import time
import threading

def mainserver(ip, port):
    ThreadsLock = threading.Lock()
    ThreadsList = []

    server = Server()
    server.start(ip, port)

    while True:
       server.listen(10)
       ClientSocket = server.accept()
       t1 = ServerThread()
       t1.run(server, ClientSocket)




if __name__ == "__main__":
    ip='0.0.0.0'
    port=45
    addr = ((ip, port))
    mainserver(ip, port)
