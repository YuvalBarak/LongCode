import socket
def Connect(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    return s

def Client(ip, port):
    s = Connect(ip, port)
    while True:
        try:
            txt = raw_input()
            s.send(txt)
            if txt == 'quit':
                s.close()
                break
        except:
            break

    

if __name__ == "__main__":
    ip='127.0.0.1'
    port=45
    Client(ip, port)
