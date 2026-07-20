from colorama import Fore, Style, init


init(autoreset=True)


def get_protocol_color(protocol):

    colors = {
        "TCP": Fore.GREEN,
        "UDP": Fore.CYAN,
        "ICMP": Fore.YELLOW,
        "ARP": Fore.MAGENTA,
        "DNS": Fore.BLUE,
        "HTTP": Fore.LIGHTGREEN_EX,
        "HTTPS": Fore.LIGHTCYAN_EX,
        "Unknown": Fore.RED
    }

    return colors.get(protocol, Fore.WHITE)


def print_table_header():

    print()

    print("-" * 115)

    print(
        f"{'Protocol':<10}"
        f"{'Source IP':<18}"
        f"{'Destination IP':<18}"
        f"{'Src Port':<10}"
        f"{'Dst Port':<10}"
        f"{'Size(Bytes)':<12}"
    )

    print("-" * 115)


def display_packet(packet_info):

    protocol = packet_info["protocol"]

    color = get_protocol_color(protocol)

    print(

        color +

        f"{protocol:<10}"
        f"{packet_info['source_ip']:<18}"
        f"{packet_info['destination_ip']:<18}"
        f"{str(packet_info['source_port']):<10}"
        f"{str(packet_info['destination_port']):<10}"
        f"{packet_info['packet_size']:<12}"

        +

        Style.RESET_ALL

    )


def print_summary(summary):

    print("\n")

    print("=" * 60)
    print("Capture Summary")
    print("=" * 60)

    print(f"Total Packets       : {summary['total_packets']}")
    print(f"Total Bytes         : {summary['total_bytes']}")
    print(f"Capture Duration    : {summary['capture_duration']} Seconds")
    print(f"Average Packet Size : {summary['average_packet_size']} Bytes")

    print("\nProtocol Distribution")

    print("-" * 60)

    for protocol, count in summary["protocol_distribution"].items():

        print(f"{protocol:<15}{count}")

    print("\nTop Source IPs")

    print("-" * 60)

    for ip, count in summary["top_source_ips"]:

        print(f"{ip:<20}{count}")

    print("\nTop Destination IPs")

    print("-" * 60)

    for ip, count in summary["top_destination_ips"]:

        print(f"{ip:<20}{count}")

    print("=" * 60)