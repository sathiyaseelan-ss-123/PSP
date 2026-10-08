import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))

server.listen(1)

print("Server is waiting for connection...")

connection, address = server.accept()

print("Connected by:", address)

message = connection.recv(1024).decode()

print("Message received:", message)

connection.close()

server.close()