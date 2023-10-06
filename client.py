import _thread
import socket

username = input('Enter your username: ') # Get the client's username

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP/IP socket object
client.connect(('127.0.0.1', 65432)) # Connect to the server

def receive():
    while True: # Infinite loop
        try: 
            message = client.recv(1024).decode('ascii') 
            if message == 'USERNAME': 
                client.send(username.encode('ascii'))
            else: 
                print(message) # Print the message
        except: 
            print('An error occured!') 
            client.close() 
            break 


def write():
    while True: # Infinite loop
        message = f'{username}: {input("")}'
        client.send(message.encode('ascii')) 


_thread.start_new_thread(receive, ()) 
_thread.start_new_thread(write, ())