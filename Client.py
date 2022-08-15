import socket
import _thread

SERVER_IP = input("What is the IP of your chat server?")

try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.bind(("0.0.0.0", 9999))
    clientSocket.connect((SERVER_IP, 9999))
except Exception as e:
    print("Exception occurred:", e)
    clientSocket.close()
else:
    print("Successfully connected!")

def sendMsg ():
    try:
        while True:
            msg = input("What would you like to send? Type exit() to leave.")
            if msg == "exit()":
                clientSocket.close()
                break
            clientSocket.send("<",  msg.encode('ascii'))
            print("Message sent!")
    except Exception as e:
        print("Connection closed or interrupted.")
        clientSocket.close()
        print(e)

def readMsg ():
    while True:
        latestMsg = clientSocket.recv(4096).decode('ascii')
        print("Message recieved:", latestMsg)

_thread.start_new_thread(sendMsg, ())
_thread.start_new_thread(readMsg, ())
