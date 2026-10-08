import socket
import time

HOST = "127.0.0.1"
PORT = 6000

number_of_connections = 10

for i in range(number_of_connections):

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))

        print("Connection", i + 1, "successful")

        client.close()

    except Exception as e:
        print("Connection failed:", e)

    time.sleep(0.2)

print("Controlled connection test completed.")