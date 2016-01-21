import time
import threading
import socket

class ServerThread (threading.Thread):
    counter = 0

    def __init__(self):
        threading.Thread.__init__(self)
        ServerThread.counter += 1

    def run(self, server, client):
        print('new connection' + str(ServerThread.counter))
        while True:
            try:
                data = client.recv(1024)
                print('user' + str(ServerThread.counter) + ': ' + data)
                if data == 'quit':
                    client.close()
                    ('end connection' + str(ServerThread.counter))
                    break
            except:
                break



class Server ():
    def __init__(self):
        self.SocketsList = []

    def start(self, ip, port):
        serversocket = socket.socket()
        serversocket.bind((ip, port))
        self.ServerSocket = serversocket

    def listen(self, maxclient):
        self.ServerSocket.listen(maxclient)

    def accept(self):
        clientsocket , addr = self.ServerSocket.accept()
        self.SocketsList.append(clientsocket)
        return clientsocket
