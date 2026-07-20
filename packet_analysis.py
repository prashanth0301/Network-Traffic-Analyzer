from scapy.all import IP, TCP, UDP, ICMP, ARP, DNS


def analyze_packet(packet):
    """
    Analyze a captured packet.

    Parameters
    ----------
    packet : scapy.packet.Packet

    Returns
    -------
    dict
        Packet information.
    """

    packet_info = {
        "protocol": "Unknown",
        "source_ip": "N/A",
        "destination_ip": "N/A",
        "source_port": "-",
        "destination_port": "-",
        "packet_size": len(packet)
    }

    # -----------------------------
    # ARP Packet
    # -----------------------------
    if packet.haslayer(ARP):

        packet_info["protocol"] = "ARP"
        packet_info["source_ip"] = packet[ARP].psrc
        packet_info["destination_ip"] = packet[ARP].pdst

        return packet_info

    # -----------------------------
    # IP Packet
    # -----------------------------
    if packet.haslayer(IP):

        packet_info["source_ip"] = packet[IP].src
        packet_info["destination_ip"] = packet[IP].dst

        # ICMP
        if packet.haslayer(ICMP):

            packet_info["protocol"] = "ICMP"

        # TCP
        elif packet.haslayer(TCP):

            packet_info["protocol"] = "TCP"

            packet_info["source_port"] = packet[TCP].sport
            packet_info["destination_port"] = packet[TCP].dport

            # HTTP
            if packet[TCP].sport == 80 or packet[TCP].dport == 80:
                packet_info["protocol"] = "HTTP"

            # HTTPS
            elif packet[TCP].sport == 443 or packet[TCP].dport == 443:
                packet_info["protocol"] = "HTTPS"

        # UDP
        elif packet.haslayer(UDP):

            packet_info["protocol"] = "UDP"

            packet_info["source_port"] = packet[UDP].sport
            packet_info["destination_port"] = packet[UDP].dport

            # DNS
            if packet.haslayer(DNS):

                packet_info["protocol"] = "DNS"

    return packet_info