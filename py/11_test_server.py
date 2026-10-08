import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 8000))
server.listen(5)

print("Test server running on port 6000")

while True:
    connection, address = server.accept()

    print("Connection received from:", address)

    connection.send(b"Connection accepted\n")
    connection.close()