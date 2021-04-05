import socket
import sys

PORT = 33000

BUFFER = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('', PORT))

user = input("Wpisz swoją nazwę użytkownika: ").encode("utf8")
client_socket.send(user)
data = 1
while data != 0:
    data = input("MSG: ")
    client_socket.send(data.encode("utf8"))
    msg = client_socket.recv(BUFFER).decode("utf8")
    print("Server> "+ msg)