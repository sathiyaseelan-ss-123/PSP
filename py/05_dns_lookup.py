import socket
domain = input("Enter domain name: ")

try:
    ip_address = socket.gethostbyname(domain)

    print("Domain:", domain)
    print("IP Address:", ip_address)

except socket.gaierror:
    print("Unable to find the IP address.")