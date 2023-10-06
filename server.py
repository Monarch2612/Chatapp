import _thread
import socket

host = '127.0.0.1' 
port = 65432 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port)) 

server.listen(2) 

clients = [] 
usernames = [] 

def broadcast(message):
    for client in clients: 
        client.send(message) 

def handle_client(client):
    while True: # Infinite loop
        try: 
            message = client.recv(1024) 
            broadcast(message) 
        except: # If there is an error
            index = clients.index(client) 
            clients.remove(client) 
            client.close() 
            username = usernames[index] 
            broadcast(f'{username} has left the chat room!'.encode('ascii')) # Broadcast that the client has left the chat room
            usernames.remove(username) 
            break 


def receive():
    while True: # Infinite loop
        client, address = server.accept() 
        print(f'Connected with {str(address)}') 

        client.send('USERNAME'.encode('ascii')) 
        username = client.recv(1024).decode('ascii') 
        usernames.append(username) 
        clients.append(client)

        print(f'Username of the client is {username}!') 
        broadcast(f'{username} has joined the chat room!'.encode('ascii')) 
        client.send('Connected to the server!'.encode('ascii')) 

        _thread.start_new_thread(handle_client, (client, )) 


print('Server is listening...') 
receive() 