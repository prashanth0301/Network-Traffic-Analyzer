import csv
import os
from datetime import datetime


REPORT_FOLDER = "reports"
PACKET_CSV_FILE = None


def create_report_directory():

    os.makedirs(REPORT_FOLDER, exist_ok=True)


def generate_timestamp():

    return datetime.now().strftime("%Y%m%d_%H%M%S")

def initialize_packet_csv():

    global PACKET_CSV_FILE

    create_report_directory()

    filename = (
        f"captured_packets_{generate_timestamp()}.csv"
    )

    filepath = os.path.join(REPORT_FOLDER, filename)

    csv_file = open(
        filepath,
        "w",
        newline="",
        encoding="utf-8"
    )

    writer = csv.writer(csv_file)

    writer.writerow([
        "Protocol",
        "Source IP",
        "Destination IP",
        "Source Port",
        "Destination Port",
        "Packet Size"
    ])

    PACKET_CSV_FILE = (csv_file, writer)

    return filepath

def save_packet(packet_info):

    if PACKET_CSV_FILE is None:
        return

    _, writer = PACKET_CSV_FILE

    writer.writerow([
        packet_info["protocol"],
        packet_info["source_ip"],
        packet_info["destination_ip"],
        packet_info["source_port"],
        packet_info["destination_port"],
        packet_info["packet_size"]
    ])

def close_packet_csv():

    global PACKET_CSV_FILE

    if PACKET_CSV_FILE is None:
        return

    csv_file, _ = PACKET_CSV_FILE

    csv_file.close()

    PACKET_CSV_FILE = None

def save_text_report(summary):

    create_report_directory()

    filename = f"traffic_summary_{generate_timestamp()}.txt"
    filepath = os.path.join(REPORT_FOLDER, filename)

    with open(filepath, "w", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write("NETWORK TRAFFIC ANALYSIS REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write(f"Total Packets        : {summary['total_packets']}\n")
        file.write(f"Total Bytes          : {summary['total_bytes']}\n")
        file.write(f"Capture Duration     : {summary['capture_duration']} Seconds\n")
        file.write(f"Average Packet Size  : {summary['average_packet_size']} Bytes\n\n")

        file.write("Protocol Distribution\n")
        file.write("-" * 60 + "\n")

        for protocol, count in summary["protocol_distribution"].items():
            file.write(f"{protocol:<15} : {count}\n")

        file.write("\nTop Source IP Addresses\n")
        file.write("-" * 60 + "\n")

        for ip, count in summary["top_source_ips"]:
            file.write(f"{ip:<20} : {count}\n")

        file.write("\nTop Destination IP Addresses\n")
        file.write("-" * 60 + "\n")

        for ip, count in summary["top_destination_ips"]:
            file.write(f"{ip:<20} : {count}\n")

    return filepath


def save_csv_report(summary):

    create_report_directory()

    filename = f"traffic_report_{generate_timestamp()}.csv"
    filepath = os.path.join(REPORT_FOLDER, filename)

    with open(filepath, "w", newline="", encoding="utf-8") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow(["Metric", "Value"])

        writer.writerow(["Total Packets", summary["total_packets"]])
        writer.writerow(["Total Bytes", summary["total_bytes"]])
        writer.writerow(["Capture Duration", summary["capture_duration"]])
        writer.writerow(["Average Packet Size", summary["average_packet_size"]])

        writer.writerow([])
        writer.writerow(["Protocol", "Packets"])

        for protocol, count in summary["protocol_distribution"].items():
            writer.writerow([protocol, count])

        writer.writerow([])
        writer.writerow(["Top Source IP", "Packets"])

        for ip, count in summary["top_source_ips"]:
            writer.writerow([ip, count])

        writer.writerow([])
        writer.writerow(["Top Destination IP", "Packets"])

        for ip, count in summary["top_destination_ips"]:
            writer.writerow([ip, count])

    return filepath