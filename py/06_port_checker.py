import socket

host = input("Enter host (example: 127.0.0.1): ")
port = int(input("Enter port number: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

try:
    result = sock.connect_ex((host, port))

    if result == 0:
        print("Port", port, "is OPEN.")
    else:
        print("Port", port, "is CLOSED or unavailable.")

except Exception as e:
    print("Error:", e)

finally:
    sock.close()