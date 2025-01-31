import socket
from threading import Thread

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",5555))


server.listen()
all_clients = {}

def client_thread (client):
    while True:
        msg = client.recv(1024)
        for c in all_clients:
           c.send(msg)
    


while True:
    print("waiting for connection...")
    client, address = server.accept()
    print("connection established:")

    name =  client.recv(1024).decode()
    all_clients[client] = name


    thread = Thread(target=client_thread,args=(client,))
    thread.start()


