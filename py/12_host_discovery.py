import socket

# Authorized local lab range
network_prefix = "127.0.0."
start = 1
end = 10

print("Checking hosts...")

for host_number in range(start, end + 1):

    ip = network_prefix + str(host_number)

    try:
        hostname = socket.gethostbyaddr(ip)[0]
        print(ip, "responds -", hostname)

    except socket.herror:
        # 127.0.0.1 is normally available
        if ip == "127.0.0.1":
            print(ip, "responds")

print("Host discovery completed.")