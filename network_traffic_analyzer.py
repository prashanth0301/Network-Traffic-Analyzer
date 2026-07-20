from interface_selection import select_interface
from packet_capture import start_packet_capture
from packet_analysis import analyze_packet
from statistics import TrafficStatistics
from packet_utils import (
    print_table_header,
    display_packet,
    print_summary
)
from report_generator import (
    initialize_packet_csv,
    save_packet,
    close_packet_csv,
    save_text_report
)


statistics = TrafficStatistics()


def process_packet(packet):

    packet_info = analyze_packet(packet)

    statistics.update(packet_info)

    save_packet(packet_info)
    display_packet(packet_info)


def select_capture_filter():

    filters = {
        1: ("ALL", None),
        2: ("TCP", "tcp"),
        3: ("UDP", "udp"),
        4: ("ICMP", "icmp"),
        5: ("ARP", "arp")
    }

    print("\nCapture Filters")
    print("-" * 30)

    for number, (name, _) in filters.items():
        print(f"{number}. {name}")

    while True:

        try:

            choice = int(input("\nSelect Filter : "))

            if choice in filters:
                return filters[choice][1]

            print("Invalid selection.")

        except ValueError:

            print("Enter a valid number.")

def main():

    print("=" * 65)
    print("           NETWORK TRAFFIC ANALYZER")
    print("=" * 65)

    interface = select_interface()
    capture_filter = select_capture_filter()

    while True:

        try:

            packet_limit = int(
                input(
                    "\nEnter number of packets to capture (0 = Unlimited): "
                )
            )

            if packet_limit >= 0:
                break

            print("Please enter 0 or a positive number.")

        except ValueError:

            print("Invalid input. Enter a numeric value.")

    packet_csv = initialize_packet_csv()

    print_table_header()

    start_packet_capture(
        interface=interface,
        packet_handler=process_packet,
        packet_limit=packet_limit,
        capture_filter=capture_filter
    )

    close_packet_csv()

    summary = statistics.get_summary()

    print_summary(summary)

    txt_report = save_text_report(summary)

    print("\nReports Generated Successfully")
    print(f"Summary Report : {txt_report}")
    print(f"Packet Report  : {packet_csv}")


if __name__ == "__main__":

    main()