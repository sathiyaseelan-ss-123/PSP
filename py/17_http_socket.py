import socket

host = "example.com"
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((host, port))

    request = (
        "GET / HTTP/1.1\r\n"
        "Host: example.com\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    client.sendall(request.encode())

    response = b""

    while True:
        data = client.recv(4096)

        if not data:
            break

        response += data

    print(response.decode(errors="ignore"))

except Exception as e:
    print("Error:", e)

finally:
    client.close()