import socket
import threading

HOST = "127.0.0.1"
PORT = 7000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

print("Connected to chat server.")


def receive_messages():

    while True:
        try:
            message = client.recv(1024).decode()

            if message:
                print("\nMessage:", message)

        except:
            break


thread = threading.Thread(
    target=receive_messages,
    daemon=True
)

thread.start()

while True:

    message = input("You: ")

    if message.lower() == "exit":
        break

    client.send(message.encode())

client.close()