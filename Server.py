import socket
import _thread

# TODO: Add exception planning in case of connection issues between client(s) and server

serverScoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverScoket.bind("0.0.0.0", 9999)
serverScoket.listen()

clients = []

def addConnection():
    while True:
        clientSocket, clientAddr = serverScoket.accept()
        print("Connected with", clientAddr)

        clients.append((clientSocket, clientAddr))

def broadcast(msg):
    for client in clients:
        client[0].send(client[1], "said:", msg.encode('ascii'))

def read():
    while True:
        msg = serverSocket.recv(2048).decode('ascii')
        broadcast("msg")

_thread.start_new_thread(addConnection, ())
_thread.start_new_thread(read, ())
