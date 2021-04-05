import socket
import sys

PORT = 33000

BUFFER = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', PORT))
server_socket.listen(2)

while True:
	client_socket, address = server_socket.accept()

	print(f"Nowe połączenie z {address[0]}:{address[1]}!!!")

	username = client_socket.recv(BUFFER).decode("utf8")
	print(f"Uzyskana nazwa użytkownika: {username}")

	greeting = "Witaj na serwerze PYTHON 3.7!".encode("utf8")
	cos = (f"Nazwa: {username}").encode("utf8")

	client_socket.send(greeting+cos)