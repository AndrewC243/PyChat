import socket
import _thread

serverScoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverScoket.bind("0.0.0.0", 9999)
serverScoket.listen()

clients = []

def snedMsg():
    while True:
        clientSocket, clientAddr = serverScoket.accept()
        print("Connected with", clientAddr)

        clients.append((clientSocket, clientAddr))

        