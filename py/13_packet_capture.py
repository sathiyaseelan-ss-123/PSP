from scapy.all import sniff, IP


def show_packet(packet):

    if IP in packet:

        source = packet[IP].src
        destination = packet[IP].dst
        protocol = packet[IP].proto

        print("Source      :", source)
        print("Destination :", destination)
        print("Protocol    :", protocol)
        print("-" * 40)


print("Capturing 10 packets...")

sniff(
    count=10,
    prn=show_packet,
    filter="ip"
)

print("Packet capture completed.")